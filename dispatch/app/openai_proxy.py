"""
OpenAI API Proxy Server

This module implements a proxy server for OpenAI API requests using FastAPI.
It provides rate limiting, error handling, and request/response logging.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import httpx
import os
import logging
from typing import Optional, Dict, Any
import time
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="OpenAI API Proxy")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
# Configuration
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
# PROXY_API_KEY = os.getenv("PROXY_API_KEY")  # Your proxy's API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Your OpenAI API key

print(OPENAI_API_BASE)
print(OPENAI_API_KEY)

# OPENAI_API_BASE = "https://api.openai.com/v1"
# OPENAI_API_BASE = "https://fzdlfltvyzatf8-8888.proxy.runpod.net/v1"
# OPENAI_API_BASE = "http://0.0.0.0:8000/v1"
# OPENAI_API_KEY = "token-abc123"
# PROXY_API_KEY = None


async def forward_request(
    request: Request,
    path: str,
    client: httpx.AsyncClient
) -> StreamingResponse:
    """
    Forward the request to OpenAI API and stream the response back.

    Args:
        request (Request): The incoming FastAPI request
        path (str): The API endpoint path
        client (httpx.AsyncClient): The HTTP client for making requests

    Returns:
        StreamingResponse: Streamed response from OpenAI
    """
    try:
        # Get request body and headers
        body = await request.json() if await request.body() else None
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }

        # Log the incoming request
        logger.info(f"Incoming request to {path}")
        
        # Forward the request to OpenAI
        url = f"{OPENAI_API_BASE}/{path}"
        response = await client.request(
            method=request.method,
            url=url,
            json=body,
            headers=headers,
            timeout=60.0
        )

        # Stream the response back
        return StreamingResponse(
            response.aiter_bytes(),
            status_code=response.status_code,
            media_type=response.headers.get("content-type")
        )

    except Exception as e:
        logger.error(f"Error forwarding request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# @app.middleware("http")
# async def api_key_validator(request: Request, call_next):
#     """
#     Middleware to validate the API key in the request header.
#     """
#     if PROXY_API_KEY:
#         api_key = request.headers.get("x-api-key")
#         if not api_key or api_key != PROXY_API_KEY:
#             raise HTTPException(status_code=401, detail="Invalid API key")
#     return await call_next(request)

# @app.on_event("startup")
# async def startup():
#     """Initialize the HTTP client on startup."""
#     app.state.client = httpx.AsyncClient()

# @app.on_event("shutdown")
# async def shutdown():
#     """Close the HTTP client on shutdown."""
#     await app.state.client.aclose()

# Route handlers for different OpenAI endpoints
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_endpoint(request: Request, path: str):
    """
    Generic endpoint that forwards all requests to OpenAI API.
    
    Args:
        request (Request): The incoming FastAPI request
        path (str): The API endpoint path
    """
    return await forward_request(request, path, app.state.client)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 