from fastapi import Query, HTTPException
from models.enums.repository_sort_field import RepositorySortField

def get_user_name(username:str = Query(..., min_length=1)) -> str:
    
    username = username.strip()
    
    # TODO add regex for username format
    
    if not username:
        raise HTTPException(
            status_code=422,
            detail="Invalid username"
        )
    
    return username


def get_repo_name(repo_name:str = Query(..., min_length=1)) -> str:
    
    repo_name = repo_name.strip()
    
    if not repo_name:
        raise HTTPException(
            status_code=422,
            detail="Invalid repository name"
        )
    
    return repo_name