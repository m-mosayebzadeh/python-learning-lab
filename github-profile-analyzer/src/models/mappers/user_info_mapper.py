from models.responses.user_info_response import UserInfoResponse

def to_user_info_response(user:dict) -> UserInfoResponse:
    
    return UserInfoResponse(
        username = user.get("login"),
        name = user.get("name") or "",
        bio = user.get("bio") or "",
        followers = user.get("followers"),
        following = user.get("following"),
        public_repos = user.get("public_repos"),
        date_of_membership = user.get("created_at")
    )