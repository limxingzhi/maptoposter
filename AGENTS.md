# AGENTS.md

## Rules

- **Always smoke-test functional changes before marking tasks complete.**
  - For the HTTP server: start uvicorn, hit the endpoint with curl, verify a 200 response and valid image output.
  - For the CLI: run the command and verify expected output.
- Run `python -m compileall . -q` after editing Python files to catch syntax errors.
- Do not commit unless explicitly asked.
- Follow the existing code style: no comments unless requested.

## Testing the HTTP Server

```bash
uvicorn server:app --host 127.0.0.1 --port 8199 &
sleep 3
curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:8199/poster?city=Paris&country=France"
# Expected: 200
curl -s "http://127.0.0.1:8199/themes" | python -m json.tool
# Expected: JSON with themes list
kill %1
```
