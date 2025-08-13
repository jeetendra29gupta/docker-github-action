# docker-github-action

This project demonstrates how to build and test a FastAPI application using Docker and GitHub Actions.

---

## 🧱 Tech Stack

- Python 3.11
- FastAPI
- Docker
- GitHub Actions
- Pytest

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/jeetendra29gupta/docker-github-action.git
cd docker-github-action
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### 📦 Build Docker Image

```bash
docker build -t fastapi-app .
````

### 🐳 Run the Container

```bash
docker run -d --name my-fastapi-container -p 8181:8181 fastapi-app
```

Visit the app at: [http://localhost:8181](http://localhost:8181)

---

## ✅ Running Tests Locally

Make sure your FastAPI app is running (via Docker), then run tests using `pytest` from the host machine:

```bash
pytest
```

Your test files should live in the `tests/` directory.

---

## 🔁 GitHub Actions Workflow

This project includes a GitHub Actions workflow to:

* Build the Docker image
* Run the container
* Run `pytest` against the running FastAPI app

### 📂 Workflow File

1. Checkout code
2. Build Docker image
3. Start FastAPI container
4. Wait for service to be ready
5. Install test dependencies
6. Run `pytest`
7. Cleanup container

---

