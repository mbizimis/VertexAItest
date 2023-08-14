export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export REPO_NAME=vertex-aigcloud auth configure-docker \
    us-central1-docker.pkg.dev-test
export IMAGE_NAME=data-pipeline
export IMAGE_TAG=latest
export IMAGE_URI=us-central1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}
