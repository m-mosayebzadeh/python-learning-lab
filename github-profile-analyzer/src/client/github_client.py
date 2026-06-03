import requests
from requests import Timeout, ConnectionError, RequestException
import config
from fastapi import HTTPException

class GitHubClient:
    
    BASE_URL = "https://api.github.com"
    
    def safe_get(self, url:str, headers:dict | None = None, timeout:int | None = config.DEFAULT_TIMEOUT, params:dict | None = None):
        
        try:
            response = requests.get(url, headers=headers, timeout=timeout, params=params)
            
            self.validate_response(response)
            
            return response.json()
            
        except Timeout:
            raise HTTPException(504, "timeout")
        
        except ConnectionError:
            raise HTTPException(503, "connection error")

        except RequestException as e:
            raise HTTPException(502, f"GitHub API request failed: {str(e)}")
            

    def get_headers(self):
        return {
            "Accept": config.ACCEPT_HEADER,
            "X-GitHub-Api-Version": config.API_VERSION,
            "Authorization": f"Bearer {config.GITHUB_TOKEN}"
        }
        

    def call_user_info(self, username:str):

        url = f"{self.BASE_URL}/users/{username}"

        return self.safe_get(url, headers=self.get_headers())


    def call_user_repositories(self, username:str, page:int, page_size:int):
            
        url = f"{self.BASE_URL}/users/{username}/repos"

        params = {
            "page": page,
            "per_page": page_size
        }
        
        return self.safe_get(url, headers=self.get_headers(), params=params)


    def call_repo_language(self, username:str, repo_name:str):
        
        url = f"{self.BASE_URL}/repos/{username}/{repo_name}/languages"
        
        return self.safe_get(url, headers= self.get_headers())


    def validate_response(self, response:requests.Response):
        
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
        elif response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="Rate Limit Exceeded"
            )
        elif response.status_code == 404:
            raise HTTPException(
                status_code=response.status_code,
                detail="Resource Not Found"
            )
        else:
            response.raise_for_status()
            