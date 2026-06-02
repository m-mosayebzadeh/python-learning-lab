import requests
import config
from fastapi import HTTPException

def get_headers():
    return {
        "Accept": config.ACCEPT_HEADER,
        "X-GitHub-Api-Version": config.API_VERSION,
        "Authorization": f"Bearer {config.GITHUB_TOKEN}"
    }
    

def call_user_info(username:str):
    
    headers = get_headers()

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, headers=headers, timeout=10)
    error_handler(response)
    
    return response.json()

def call_user_repositories(username:str):
        
    headers = get_headers()

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url, headers=headers, timeout=10)
    error_handler(response)
    
    return response.json()


def call_repo_language(username:str, repo_name:str):
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/languages"
    
    response = requests.get(url, headers= get_headers())
    error_handler(response)
    
    return response.json()


def error_handler(response:requests.Response):
    
    if response.status_code == 401:
        raise HTTPException(
            status_code = response.status_code,
            detail="Invalid Token"
        )
    elif response.status_code == 403:
        raise HTTPException(
            status_code=response.status_code,
            detail="Rate Limit"
        )
    elif response.status_code == 404:
        raise HTTPException(
            status_code=response.status_code,
            detail="Resource Not Found"
        )
    else:
        response.raise_for_status()
        