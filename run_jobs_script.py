from google.cloud import aiplatform


if __name__ == '__main__':
    aiplatform.init(location="us-central1")

    job = aiplatform.CustomContainerTrainingJob(
        display_name="data-pipeline-remote",
        container_uri="us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/data-pipeline@sha256:8f6b11757899d2e8315011a9cd9de60c9b3b084f3d6f737a82f5e8f5148468ad",
        staging_bucket="ai_repo/VertextAI_test/staging_test",
    )

    print('Running job...')
    res = job.run(
        replica_count=1,
        machine_type='n1-standard-4',
        args=[]
    )
    print(f'Done:\n{res}')
