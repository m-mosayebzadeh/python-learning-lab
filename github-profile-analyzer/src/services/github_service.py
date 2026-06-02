from client import github_client as github_client
from models.responses.user_info_response import UserInfoResponse
from models.responses.repository_response import RepositoryResponse
from models.responses.language_usage_response import LanguageUsageResponse

def get_user_info(username:str) -> UserInfoResponse:

    user = github_client.call_user_info(username)

    return UserInfoResponse(
        username = user.get("login"),
        name = user.get("name") or "",
        bio = user.get("bio") or "",
        followers = user.get("followers"),
        following = user.get("following"),
        public_repos = user.get("public_repos"),
        date_of_membership = user.get("created_at")
    )



def get_repositories(username:str) -> list[RepositoryResponse]:
    
    git_repositories = github_client.call_user_repositories(username)

    repositories = []

    for repo in git_repositories:

        if not repo.get("private"):
            repositories.append(
                RepositoryResponse(
                    name = repo.get("name"),
                    star_count = repo.get("stargazers_count"),
                    forks_count = repo.get("forks_count"),
                    language = repo.get("language"),
                    created_at = repo.get("created_at"),
                    updated_at = repo.get("updated_at")
                )
            )

    return repositories


def get_popular_repositories(username:str, sort_item_list: list[str]) -> list[RepositoryResponse]:

    repositories = get_repositories(username)
    
    sorted_item = sorted(
        repositories,
        key=lambda item: tuple(item[field] for field in sort_item_list),
        reverse=True
    )

    return sorted_item

def get_language_usage(username:str, repo_name:str) -> list[LanguageUsageResponse]:
    
    res = github_client.call_repo_language(username, repo_name)
    
    language_percent = []
    
    if res:
        total_bytes = sum(res.values())
        
        for lang, bytes in res.items():
            language_percent.append(
                LanguageUsageResponse(
                    language = lang,
                    usage = round((bytes / total_bytes) * 100, 1)
            ))
            
    return language_percent
