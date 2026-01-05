from fastapi import FastAPI, Response, Request
import subprocess
import sys

app = FastAPI()

@app.post("/rephrase")
async def rephrase(request: Request):
    body = await request.body()
    text = body.decode("utf-8")

    result = subprocess.run(
        [sys.executable, "rephrase.py"],
        input=text,
        text=True,
        capture_output=True
    )

    return Response(
        content=result.stdout,
        media_type="text/plain; charset=utf-8"
    )
