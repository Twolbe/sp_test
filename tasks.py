import os
from invoke import Collection, task

compose_file_name = {
    "dev": 'docker-compose.dev.yaml',
    "prod": 'docker-compose.prod.yaml'
}

os.environ["API_SU_MODE"] = "prod"
os.environ["API_PU_MODE"] = "prod"
os.environ["FRONT_MODE"] = "prod"

@task(iterable=['d'])
def up(ctx, d):
    if 'front' in d:
        os.environ["FRONT_MODE"] = "dev"
    if 'api_su' in d:
        os.environ["API_SU_MODE"] = "dev"
    if 'api_pu' in d:
        os.environ["API_PU_MODE"] = "dev"
    ctx.run(f'docker-compose -f "docker-compose.yaml" up -d --build')


@task
def down(ctx):
    ctx.run(f'docker-compose -f "docker-compose.yaml" down')
