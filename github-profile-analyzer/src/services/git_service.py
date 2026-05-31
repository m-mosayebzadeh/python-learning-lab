import requests
import config
from fastapi import HTTPException


def get_headers():
    return {
        "Accept": config.ACCEPT_HEADER,
        "X-GitHub-Api-Version": config.API_VERSION,
        "Authorization": f"Bearer {config.GITHUB_TOKEN}"
    }

def get_user_info(username:str):

    headers = get_headers()

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()


    user = response.json()

    return {
        "username" : user.get("login"),
        "name" : user.get("name") or "",
        "bio" : user.get("bio") or "",
        "followers" : user.get("followers"),
        "following" : user.get("following"),
        "public_repos" : user.get("public_repos"),
        "date_of_membership" : user.get("created_at")
    }



def get_repositories(username:str):
    
    headers = get_headers()

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    repositories = []

    for repo in response.json():

        if not repo.get("private"):
            repositories.append({
                "name" : repo.get("name"),
                "star_count" : repo.get("stargazers_count"),
                "forks_count" : repo.get("forks_count"),
                "language" : repo.get("language"),
                "created_at" : repo.get("created_at"),
                "updated_at" : repo.get("updated_at")
            })

    return repositories


def get_popular_repositories(username:str, sort_item_list: list[str]):

    allowed_sort_fields = ["star_count", "forks_count"]

    invalid_items = [item for item in sort_item_list if item not in allowed_sort_fields]
  
    # TODO transfer to api layer 
    if invalid_items:
        raise HTTPException(
            status_code= 422,
            detail= f"invalid sort fields : {",".join(invalid_items)}"
        )
    

    repositories = get_repositories(username)
    sorted_item = sorted(
        repositories,
        key=lambda item: tuple(item[field] for field in sort_item_list),
        reverse=True
    )

    return sorted_item
    
