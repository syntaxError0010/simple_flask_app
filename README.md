# Fork and Clone this repo

# To run the app on local python runtime
## Step 1: Create a Python venv

```python
python3 -m venv .venv
```

Activate the venv

```bash
. .venv/bin/activate # For Linux
.venv\Scripts\activate.bat # For Windows
```

## Step 2: Install Python Dependencies

```python
pip install -r requirements.txt
```

## Step 3: Run the server

```python
python3 app.py
```

# To run the app on local docker

## Build the image if not already

```bash
docker build -t simple-flask-app .
```

## Run the Docker image

```bash
docker run -p 5000:5000   -e APP_NAME="HelloWorld"   -e APP_ENV="production"   -e APP_AUTHOR="Jane Doe"   -e SECRET_KEY="super-secret-xyz"   simple-flask-app
```

# To run it on GitHub Actions


Step 1: Create a docker hub account

Step 2: Create a PAT for your docker hub account

Step 3: Create a Docker Hub repository (public) with name `simple-flask-app`

Step 4: Create secrets and variables in GitHub Repo

Step 5: On your forked repo, create secrets and variables

GitHub has two places to store this — **Secrets** (encrypted, for sensitive values) and **Variables** (plain text, for non-sensitive config). Here's exactly how to set up both.

---

### Secrets — for sensitive values

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **Secrets tab** → click **New repository secret**.

Add each of these:

| Name | Value |
|---|---|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token (see below) |
| `EC2_USER` | SSH user, e.g. `ubuntu` or `ec2-user` |
| `EC2_SSH_KEY` | Your full `.pem` file contents (see below) |
| `EC2_PORT` | `22` (unless you changed it) |
| `SECRET_KEY` | Your Flask secret key |
| `APP_NAME` | e.g. `MyFlaskApp` |
| `APP_AUTHOR` | e.g. `Jane Doe` |

---

### Variables — for non-sensitive config

Same page → **Variables tab** → **New repository variable**.

| Name | Value |
|---|---|
| `EC2_HOST` | Your EC2 public IP or domain, e.g. `54.123.45.67` |

---
run1