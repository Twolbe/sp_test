from invoke import Collection, task

compose_file_name = {
    "dev": 'docker-compose.dev.yaml',
    "prod": 'docker-compose.prod.yaml'
}


@task
def up(ctx, mode):
    ctx.run(f'docker-compose -f "{compose_file_name[mode]}" up -d --build')

@task
def down(ctx, mode):
    ctx.run(f'docker-compose -f "{compose_file_name[mode]}" down')