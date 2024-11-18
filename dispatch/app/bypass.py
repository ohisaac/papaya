from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
import httpx
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

# OPENAI_API_KEY = "token-abc123"
# # OPENAI_API_BASE = "https://fzdlfltvyzatf8-8888.proxy.runpod.net/v1"
# OPENAI_API_BASE = "http://0.0.0.0:8000/v1"

async def proxy_request(request: Request, path: str):
    """
    Proxies incoming HTTP requests to OpenAI's API endpoints.
    This async function forwards requests to OpenAI while handling authentication and streaming responses.
    It preserves the original request method, headers, and body while adding OpenAI authentication if needed.
    Args:
        request (Request): The incoming FastAPI request object
        path (str): The API endpoint path to forward the request to
    Returns:
        StreamingResponse: A streaming response from the OpenAI API with preserved status code and content type
    Raises:
        HTTPException: If the request fails, returns 500 status code with error details
    """
    # Get the request body
    body = await request.json() if request.method in ["POST", "PUT"] else None
    
    # Get headers but remove host
    headers = dict(request.headers)
    headers.pop("host", None)
    
    # Set OpenAI API key if not provided in headers
    if "authorization" not in headers:
        headers["authorization"] = f"Bearer {OPENAI_API_KEY}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=f"{OPENAI_API_BASE}/{path}",
                json=body,
                headers=headers,
                timeout=60.0
            )
            
            return StreamingResponse(
                response.iter_bytes(),
                status_code=response.status_code,
                media_type=response.headers.get("content-type")
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    return await proxy_request(request, path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)