from client.github_client import GitHubClient
from models.responses.user_info_response import UserInfoResponse
from models.responses.repository_response import RepositoryResponse
from models.responses.language_usage_response import LanguageUsageResponse
from models.mappers.user_info_mapper import to_user_info_response
from models.mappers.repository_mapper import to_repository_response
from models.enums.repository_sort_field import RepositorySortField

github_client = GitHubClient()

def get_user_info(username:str) -> UserInfoResponse:

    user = github_client.call_user_info(username)
    
    return to_user_info_response(user)

def get_repositories(username:str) -> list[RepositoryResponse]:
    
    git_repositories = github_client.call_user_repositories(username)

    repositories = []

    for repo in git_repositories:
        if not repo.get("private"):
            repositories.append(to_repository_response(repo))

    return repositories


def get_popular_repositories(username:str, sort_item_list: list[RepositorySortField]) -> list[RepositoryResponse]:

    repositories = get_repositories(username)
    
    sorted_item = sorted(
        repositories,
        key=lambda item: tuple(getattr(item, field.value) for field in sort_item_list),
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
