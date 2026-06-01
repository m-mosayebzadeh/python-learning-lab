from fastapi import APIRouter
import services.git_service as git_service
from fastapi import Query

router = APIRouter()

@router.get("/user/info")
def get_user_info(username:str):
    return git_service.get_user_info(username)

@router.get("/repo/all-repo-name")
def get_all_repo_name(username:str):
    return git_service.get_repositories(username)

@router.get("/repo/popular")
def get_popular_repo(username:str, sort_item_list: list[str] = Query(default=["star_count"])):
    return git_service.get_popular_repositories(username, sort_item_list)

@router.get("/language/usage")
def get_language_usage(username:str, repo_name:str):
    return git_service.get_language_usage(username, repo_name)