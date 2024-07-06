from typing import Dict, Optional
from langchain_openai import ChatOpenAI
from langchain_community.utilities import RequestsWrapper
from pydantic import BaseModel
import yaml
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
import os
import requests
from dotenv import load_dotenv
import planner

load_dotenv()


# NOTE: In this example. We must set `allow_dangerous_request=True` to enable the OpenAPI Agent to automatically use the Request Tool.
# This can be dangerous for calling unwanted requests. Please make sure your custom OpenAPI spec (yaml) is safe.
ALLOW_DANGEROUS_REQUEST = True


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


def initialize_environment(tool: ToolResponse):
    headers = {}
    # check if we need to request for the oauth token
    if tool.token_req:
        body = tool.token_req.body
        body["client_id"] = os.environ[f'{tool.id}_CLIENT_ID']
        body["client_secret"] = os.environ[f'{tool.id}_CLIENT_SECRET']
        api_response = requests.post(
            tool.token_req.url, headers=tool.token_req.headers, data=body)
        if api_response.status_code != 200:
            raise Exception(api_response.text)
        else:
            res = api_response.json()
            headers["Authorization"] = f"Bearer {res['access_token']}"
            if tool.headers:
                headers.update(tool.headers)
    else:
        # otherwise a simple api key will suffice
        headers = tool.headers if tool.headers else {}
        if tool.header_auth:
            if tool.header_auth["type"] == "Bearer":
                headers["Authorization"] = f"Bearer {os.environ[f'{tool.id}_API_KEY']}"
            else:
                headers[tool.header_auth["key"]
                        ] = os.environ[f'{tool.id}_API_KEY']

    body = {}
    if tool.body_auth:
        body[tool.body_auth["key"]] = os.environ[f'{tool.id}_API_KEY']

    spec_file = requests.get(tool.spec_url)
    tool_specification = reduce_openapi_spec(yaml.safe_load(spec_file.text))

    return headers, tool_specification, body


def get_optimal_tool(query: str) -> ToolResponse:
    api_response = requests.post(
        "http://localhost:8000/search", json={"query": query})
    if api_response.status_code != 200:
        raise Exception(api_response.text)

    return ToolResponse(**api_response.json())


llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0)

user_query = (
    "what is a 2012 song from drake on spotify"
)

tool = get_optimal_tool(user_query)
headers_env, tool_spec, body = initialize_environment(tool)

print(body, type(body))

spotify_agent = planner.create_openapi_agent(
    tool_spec,
    RequestsWrapper(headers=headers_env),
    llm,
    body_wrapper=body,
    allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST,
)
spotify_agent.invoke(user_query)
