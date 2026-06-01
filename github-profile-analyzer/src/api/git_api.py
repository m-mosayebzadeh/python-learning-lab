from fastapi import APIRouter
import services.git_service as git_service
from api import git_depends
from fastapi import Depends

router = APIRouter()

@router.get("/user/info")
def get_user_info(username:str = Depends(git_depends.get_user_name)):
    return git_service.get_user_info(username)

@router.get("/repo/all-repo-name")
def get_all_repo_name(username:str = Depends(git_depends.get_user_name)):
    return git_service.get_repositories(username)

@router.get("/repo/popular")
def get_popular_repo(username:str = Depends(git_depends.get_user_name), sort_filter_list: list[str] = Depends(git_depends.get_sort_filter_list)):
    return git_service.get_popular_repositories(username, sort_filter_list)

@router.get("/language/usage")
def get_language_usage(username:str = Depends(git_depends.get_user_name), repo_name:str = Depends(git_depends.get_repo_name)):
    return git_service.get_language_usage(username, repo_name)