from google_cloud_pipeline_components.v1.custom_job import create_custom_training_job_from_component
from kfp import dsl, compiler
from google.cloud import aiplatform
from google_cloud_pipeline_components import v1
from kfp.components.pipeline_task import PipelineTask


@dsl.container_component
def data_component(dataset_path: dsl.OutputPath()):
    return dsl.ContainerSpec(
        image='us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/data-pipeline:latest',
        args=[],
    )


@dsl.container_component
def train_component(dataset_path: dsl.InputPath()):
    return dsl.ContainerSpec(
        image='us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/train-pipeline:latest',
        args=['--dataset_path', dataset_path]
    )


# @dsl.component(base_image='us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/data-pipeline:latest')
# def data_component_wrapper():
#     pass
#
#
# @dsl.component(base_image='us-central1-docker.pkg.dev/information-discovery/vertex-ai-test/train-pipeline:latest')
# def train_component_wrapper():
#     pass


@dsl.pipeline(
    name="data-to-train-pipeline",
    pipeline_root='gs://ai_repo/VertextAI_test'
)
def my_pipeline(project_id: str):
    # prepare data
    data_job = create_custom_training_job_from_component(
        data_component,
        display_name='data-pipeline-Op',
        replica_count=1,
        machine_type='n1-standard-4'
    )
    print(data_job)

    # run training afterwards
    train_job = create_custom_training_job_from_component(
        train_component,
        display_name='train-pipeline-Op',
        replica_count=1,
        machine_type='n1-standard-4',
        accelerator_type='',
        accelerator_count=1,
        boot_disk_type='pd-ssd',
        boot_disk_size_gb=100,
    )

    # must run jobs after declaring them else error

    print('Running data job...')
    res: PipelineTask = data_job()
    print('Done:', res)

    print("Running train job...")
    res2: PipelineTask = train_job(res.outputs['dataset_path'])
    print("Done:", res2)


# @dsl.pipeline(
#     name="data-to-train-pipeline",
#     pipeline_root='gs://ai_repo/VertextAI_test'
# )
# def my_pipeline(project_id: str):
#     data_task: PipelineTask = data_component()
#     print('Data component res:', data_task)
#
#     train_task: PipelineTask = train_component()
#     print('Train component res:', train_task)


if __name__ == '__main__':
    # compile
    compiler.Compiler().compile(pipeline_func=my_pipeline, package_path='pipeline.yaml')

    # run pipeline
    import google.cloud.aiplatform as aip

    job = aip.PipelineJob(
        display_name="custom_data_train_pipeline",
        template_path='pipeline.yaml',
        pipeline_root='gs://ai_repo/VertextAI_test',
        parameter_values={
            "project_id": "Information Discovery"
        },
    )

    job.submit()
