import hashlib
import hmac
from typing import Optional

from flask import Flask, request

app = Flask(__name__)

PASSWORD = ""


def authenticate(fivetran_request: request) -> Optional[str]:
    # Create our own hash using the request body and our password
    request_body = fivetran_request.data.decode("UTF-8")
    valid_hash: str = (
        hmac.new(
            bytes(PASSWORD, "latin-1"),
            msg=bytes(request_body, "latin-1"),
            digestmod=hashlib.sha256,
        )
        .hexdigest()
        .upper()
    )

    fivetran_hash: str = fivetran_request.headers.get("X-Fivetran-Signature-256")

    if fivetran_hash != valid_hash:
        return "Invalid Request"


@app.route("/", methods=["POST"])
def main():
    if request.method == "POST":
        auth_response = authenticate(request)
        if auth_response:
            return auth_response

        if request.json.get("event") == "sync_end":
            return "Sync end event"

    return "Unhandled event type"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
