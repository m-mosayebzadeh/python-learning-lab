from models.responses.repository_response import RepositoryResponse

def to_repository_response(repository:dict) -> RepositoryResponse:
        
    return RepositoryResponse(
        name = repository.get("name"),
        star_count = repository.get("stargazers_count"),
        forks_count = repository.get("forks_count"),
        language = repository.get("language"),
        created_at = repository.get("created_at"),
        updated_at = repository.get("updated_at")
    )
