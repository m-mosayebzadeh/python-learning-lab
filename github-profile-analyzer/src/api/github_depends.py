from fastapi import Query, HTTPException

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

def get_sort_filter_list(sort_filter_list:list[str] = Query(default=["star_count"])) -> list[str]:
    
    allowed_sort_filters = {"star_count", "forks_count"}

    invalid_items = [item.strip() for item in sort_filter_list if item.strip() not in allowed_sort_filters]
  
    
    if invalid_items:
        raise HTTPException(
            status_code= 422,
            detail= f"invalid sort fields : {",".join(invalid_items)} -> just use this list items : {allowed_sort_filters}"
        )
    
    return [item.strip() for item in sort_filter_list]