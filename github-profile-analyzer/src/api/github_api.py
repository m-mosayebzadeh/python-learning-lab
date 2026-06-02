from fastapi import APIRouter, Depends, Query
import services.github_service as git_service
from api import github_depends as github_depends
from models.responses.user_info_response import UserInfoResponse
from models.responses.repository_response import RepositoryResponse
from models.responses.language_usage_response import LanguageUsageResponse
from models.enums.repository_sort_field import RepositorySortField


router = APIRouter()

@router.get(
    "/user/info",
    response_model=UserInfoResponse
)
def get_user_info(username:str = Depends(github_depends.get_user_name)):
    return git_service.get_user_info(username)

@router.get(
    "/repo/all-repo",
    response_model=list[RepositoryResponse]
)
def get_all_repo(username:str = Depends(github_depends.get_user_name)):
    return git_service.get_repositories(username)

@router.get(
    "/repo/popular",
    response_model=list[RepositoryResponse]    
)
def get_popular_repo(username:str = Depends(github_depends.get_user_name), sort_filter_list: list[RepositorySortField] = Query(default=[RepositorySortField.STAR_COUNT])):
    return git_service.get_popular_repositories(username, sort_filter_list)

@router.get(
    "/language/usage",
    response_model=list[LanguageUsageResponse]
)
def get_language_usage(username:str = Depends(github_depends.get_user_name), repo_name:str = Depends(github_depends.get_repo_name)):
    return git_service.get_language_usage(username, repo_name)