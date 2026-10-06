# SE-490 Cloud Computing Lab: Docker + CI/CD

A small Flask app, already dockerized. Your job: put it on GitHub and build a CI/CD pipeline.

## 1. Run locally
```bash
git clone <this-repo-url>
cd cloud-lab-starter

# with Docker
docker build -t cloud-lab .
docker run -p 5000:5000 cloud-lab
# or
docker compose up --build
```
Test: http://localhost:5000/ , /health , /add?a=2&b=3

## 2. Run tests without Docker
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
flake8 app tests --max-line-length=100
```

## 3. Push to YOUR GitHub
Create an empty repo on GitHub, then:
```bash
git remote remove origin
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

## 4. Tasks
1. Complete `.github/workflows/ci.yml`:
   - Lint (flake8) and test (pytest) on every push and pull request
   - Build the Docker image only if tests pass
   - Push the image to GitHub Container Registry (ghcr.io) tagged with the commit SHA and `latest`
2. Store credentials in GitHub **Secrets**, never in code.
3. Add a status badge to this README.
4. Bonus: deploy automatically to a cloud platform after a successful push.
5. Bonus: break a test on purpose and show that the pipeline blocks the build.

## Submission
Send your GitHub repo link with a screenshot of a green pipeline run.
