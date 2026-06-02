from enum import Enum

class RepositorySortField(str, Enum):
    
    STAR_COUNT = "star_count"
    FORKS_COUNT = "forks_count"
