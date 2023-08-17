from google.cloud import aiplatform


if __name__ == '__main__':
    aiplatform.init(location="us-central1")

    job = aiplatform.CustomContainerTrainingJob(
        display_name="data-pipeline-remote",
        container_uri="us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/data-pipeline:latest",
        staging_bucket="ai_repo/VertextAI_test/staging_test",
    )

    print('Running data job...')
    res = job.run(
        replica_count=1,
        machine_type='n1-standard-4',
        args=[]
    )
    print(f'Done:\n{res}')

    job = aiplatform.CustomContainerTrainingJob(
        display_name="train-pipeline-remote",
        container_uri="us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/train-pipeline:latest",
        staging_bucket="ai_repo/VertextAI_test/staging_test",
    )

    print('Running train job...')
    res = job.run(
        replica_count=1,
        machine_type='n1-standard-4',
        args=[]
    )
    print(f'Done:\n{res}')
