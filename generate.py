import hashlib
import hmac
import json

if __name__ == "__main__":
    password = ""
    request = {
        "event": "sync_end",
        "created": "2021-09-23T14:50:34.386Z",
        "connector_type": "shopify",
        "connector_id": "clang_taught",
        "destination_group_id": "revive_turtle",
        "data": {
            "status": "FAILURE_WITH_TASK",
            "reason": "ErrorExceptionFromJava: something failed",
        },
    }
    request_string = json.dumps(request, indent=4)
    print(f"body: {request_string}")
    refinery_hash: str = (
        hmac.new(
            bytes(password, "latin-1"),
            msg=bytes(request_string, "latin-1"),
            digestmod=hashlib.sha256,
        )
        .hexdigest()
        .upper()
    )
    print(f"header: {refinery_hash}")
