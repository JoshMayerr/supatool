"""
A test implementation that selects the optimal tool to use based on an end user query.
"""

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Query(BaseModel):
    query: str


class TokenRequest(BaseModel):
    url: str
    headers: Dict[str, str]
    body: Dict[str, str]


class ToolResponse(BaseModel):
    spec_url: str
    headers: Optional[Dict[str, str]] = None
    token_req: Optional[TokenRequest] = None
    header_auth: Optional[Dict[str, str]] = None
    body_auth: Optional[Dict[str, str]] = None
    id: str


@app.get("/env_vars", response_model=List[str])
def env_vars():
    """
    Return the list of environment variables needed in the .env file.
    """

    return ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI", "NOTION_API_KEY"]


@app.get("/tools", response_model=List[ToolResponse])
def all_tools():
    """
    Return all available tools.
    """

    return None


@app.get("/tools/{tool_id}", response_model=ToolResponse)
def get_tool(tool_id: int):
    """
    Return the tool with the specified ID.
    """

    return None


@app.post("/search", response_model=ToolResponse)
def get_tool(query: Query):
    """
    @param query: The user query

    Return the optimal tool to use based on the user query.
    """

    query_str = query.query.lower()

    if "spotify" in query_str:
        spec_url = "https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/spotify.com/1.0.0/openapi.yaml"
        token_req = TokenRequest(
            url="https://accounts.spotify.com/api/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            body={"grant_type": "client_credentials"}
        )
        headers = None
        env_id = "SPOTIPY"
        header_auth = {"type:": "Bearer", "key": ""}
        body_auth = None

    elif "notion" in query_str:
        spec_url = "https://raw.githubusercontent.com/JoshMayerr/supatool-registry/main/oas/notion/api.notion.com.json"
        headers = {"Notion-Version": "2022-02-22"}
        token_req = None
        header_auth = {"type:": "Bearer", "key": ""}
        env_id = "NOTION"

    # elif "stock" in query_str or "polygon" in query_str:
    #     spec_url = "https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/polygon.io/1.0.0/swagger.yaml"
    #     headers = None
    #     token_req = None
    #     env_id = "POLYGON"
    elif "tickets" in query_str or "ticketmaster" in query_str:
        spec_url = "https://raw.githubusercontent.com/JoshMayerr/supatool-registry/main/oas/ticketmaster/discovery.json"
        headers = None
        token_req = None
        env_id = "TICKETMASTER"
        body_auth = {"type:": "custom", "key": "apikey"}
        header_auth = None
    else:
        raise HTTPException(status_code=404, detail="No suitable tool found")

    return ToolResponse(spec_url=spec_url, headers=headers, token_req=token_req, header_auth=header_auth, body_auth=body_auth, id=env_id)
