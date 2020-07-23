# Google Kubernetes Engine Demo
>> Example of github-action that automatically deploy flask server to Google Kubernetes Engine

## Main Purpose
* Simple flask server with simple test just for demo
* Github action to automatically run unit test on each push and pull request
* Github action to automatically deploy to google cloud container registry after each tag push
* Github action to automatically deploy to google kubernetes engine after each tag push

## Directory Structure
* Program
    + main.py: route
    + core.py: core logic
    + test.py: test for core logic
    + requirements.txt: dependencies
* Environmet Variable
    + .dockerenv: local docker
    + .envrc: local shell
    + containers.env of .gcloud_deployment.yaml: gke
* Settings of ignore files
    + .gitignore: ignore files of git
    + .dockerignore: ignore files of docker
* Others
    + Dockerfile: script of docker
    + gcloud_deployment.yaml: deployment and service of gke
    + .github/workflows/workflow.yaml: script of github action
    + Makefile: some handful script, readme.md

## Google Cloud Settings
1. For test just create gke cluster with only one node(g1-small) at us-central1-a
2. Add a service account with these IAM
    + Kubernetes Engine Developer
    + Service Account user
    + Cloud Storage Admin
3. Generate key from this service account and
    + Run `cat service_account_key.json | base64`
4. Set google cloud secret to github
    + secrets.GCP_PROJECT_ID: Your google cloud project id
    + secrets.GCP_SA_KEY: The base64 code generated from service account key from previous step
* Step 2, 3, 4: To grant gke deployment privilege to github action.

## Github Action Settings
See .github/workflows/workflow.yaml
* jobs.test runs unit test on every push and pull request (including tag push)
* jobs.deploy runs deploy to container registry and runs deploy to kubernetes engine on every tag push

## Development
* Add route at main.py, Add core logic at core.py, Add unit test for core at test.py
* Run `make test` for unit test
* Run `python app.py` to start local test server
* Run `curl "http://127.0.0.1:5000/entry?str1=hello&str2=world"` to test server on local 
* Git add, commit, push to trigger CI to run unit-test
* Git tag v0.1, push tag to trigger CI to run unit-test and deploy to container registry and gke
* Run `curl "https://PRODUCTION_URL/entry?str1=hello&str2=world"` to test server on production
