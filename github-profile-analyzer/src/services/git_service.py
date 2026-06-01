from client import git_client

def get_user_info(username:str):

    user = git_client.call_user_info(username)

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
    
    git_repositories = git_client.call_user_repositories(username)

    repositories = []

    for repo in git_repositories:

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

    repositories = get_repositories(username)
    
    sorted_item = sorted(
        repositories,
        key=lambda item: tuple(item[field] for field in sort_item_list),
        reverse=True
    )

    return sorted_item

def get_language_usage(username:str, repo_name:str):
    
    res = git_client.call_repo_language(username, repo_name)
    
    language_percent = []
    
    if res:
        total_bytes = sum(res.values())
        
        for lang, bytes in res.items():
            language_percent.append({
                "language": lang,
                "usage": round((bytes / total_bytes) * 100, 1)
            })
            
    return language_percent
