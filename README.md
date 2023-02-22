## Fivetran Webhook Example

To run locally:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python __init__.py
```

To test generate a request body and headers using the `generate.py` file (after replacing the password variable). With the body and header we can curl the endpoint locally:

```
curl -XPOST -H 'X-Fivetran-Signature-256: {generated-header}' -H 'Content-Type: application/json' -d '{generated-body}' 'http://127.0.0.1:8000'
```

After visiting http://127.0.0.1:8000 in a browser we should see:

```
Sync end event
```