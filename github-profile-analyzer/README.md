# GitHub Profile Analyzer

A REST API built with FastAPI that analyzes public GitHub profiles and repositories using the GitHub REST API.

This project was created as part of my Python learning journey to practice:

* FastAPI
* REST API development
* External API integration
* Layered architecture
* Dependency Injection
* DTOs and Mappers
* Error handling
* Pagination
* Environment configuration

---

# Features

### User Profile Information

Retrieve public GitHub profile information:

* Username
* Name
* Bio
* Followers
* Following
* Public repositories count
* Account creation date

---

### Repository Analysis

Retrieve repositories with:

* Repository name
* Star count
* Fork count
* Main language
* Creation date
* Last update date

---

### Repository Sorting

Sort repositories by:

* Star count
* Fork count

Supports multiple sort fields.

---

### Language Usage Analysis

Analyze programming language usage inside a repository and calculate usage percentages.

Example:

```json
[
  {
    "language": "Python",
    "usage": 78.4
  },
  {
    "language": "JavaScript",
    "usage": 21.6
  }
]
```

---

### Pagination

Repository endpoints support pagination:

```http
?page=1&page_size=10
```

---

### Error Handling

Handles common GitHub API errors:

* Invalid token
* Rate limit exceeded
* Resource not found
* Connection errors
* Request timeout

---

# Project Structure

```text
src/
├── api/
│   ├── github_api.py
│   └── github_depends.py
│
├── client/
│   └── github_client.py
│
├── services/
│   └── github_service.py
│
├── models/
│   ├── enums/
│   │   └── repository_sort_field.py
│   │
│   ├── mappers/
│   │   ├── repository_mapper.py
│   │   └── user_info_mapper.py
│   │
│   └── responses/
│       ├── user_info_response.py
│       ├── repository_response.py
│       ├── language_usage_response.py
│       └── paginated_response.py
│
├── config.py
└── main.py
```

---

# Architecture

This project follows a layered architecture:

```text
API Layer
    ↓
Service Layer
    ↓
Client Layer
    ↓
GitHub REST API
```

### API Layer

Responsible for:

* Request handling
* Dependency injection
* Response models

### Service Layer

Responsible for:

* Business logic
* Data transformation
* Sorting and processing

### Client Layer

Responsible for:

* Communication with GitHub API
* Error handling
* Request execution

### Mapper Layer

Responsible for converting raw GitHub responses into application DTOs.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/m-mosayebzadeh/python-learning-lab.git
```

Move into the project directory:

```bash
cd github-profile-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

This project requires a GitHub Personal Access Token.

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=your_github_personal_access_token
```

Example:

```env
GITHUB_TOKEN=github_pat_xxxxxxxxxxxxxxxxxxxxxxxxx
```

Without a GitHub token, GitHub API requests may be heavily rate-limited.

---

# Creating a GitHub Token

1. Open GitHub Settings
2. Navigate to Developer Settings
3. Select Personal Access Tokens
4. Generate a new token
5. Copy the token
6. Add it to your `.env` file

Never commit your token to GitHub.

Make sure `.env` is included in `.gitignore`.

---

# Running the Application

Start the server:

```bash
uvicorn main:app --reload
```

By default:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# API Endpoints

## Get User Information

```http
GET /user/info
```

Query Parameters:

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| username  | string | Yes      |

Example:

```http
GET /user/info?username=torvalds
```

---

## Get Repositories

```http
GET /repo/all-repo
```

Query Parameters:

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| username  | string | Yes      |
| page      | int    | No       |
| page_size | int    | No       |

Example:

```http
GET /repo/all-repo?username=torvalds&page=1&page_size=10
```

---

## Get Popular Repositories

```http
GET /repo/popular
```

Query Parameters:

| Parameter        | Type   | Required |
| ---------------- | ------ | -------- |
| username         | string | Yes      |
| sort_filter_list | list   | No       |
| page             | int    | No       |
| page_size        | int    | No       |

Example:

```http
GET /repo/popular?username=torvalds&sort_filter_list=star_count
```

Multiple sort fields:

```http
GET /repo/popular?username=torvalds&sort_filter_list=star_count&sort_filter_list=forks_count
```

---

## Get Language Usage

```http
GET /language/usage
```

Query Parameters:

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| username  | string | Yes      |
| repo_name | string | Yes      |

Example:

```http
GET /language/usage?username=torvalds&repo_name=linux
```

---

# Technologies Used

* Python
* FastAPI
* Requests
* Pydantic
* GitHub REST API
* python-dotenv
* Uvicorn

---

# Learning Objectives

This project was built to practice:

* FastAPI fundamentals
* REST API design
* Layered architecture
* DTO pattern
* Mapper pattern
* External API integration
* Dependency Injection
* Error handling
* Pagination
* Environment management

---

# Future Improvements

* Repository activity analysis
* Language statistics across all repositories
* Async HTTP client
* Response caching
* Unit tests
* Integration tests
* Docker support
* GitHub contribution statistics

---

# License

This project was created for educational purposes and learning backend development with Python and FastAPI.
