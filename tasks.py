"""
inv up
    Запускает компоуз в продуктовом режиме
inv up -d front 
    Запускает разработку фронта, а весь остальной компоуз в продуктовом режиме
inv up -d api_su
    Запускает разработку апи для StaffUser, а весь остальной компоуз в продуктовом режиме
inv up -d api_pu
    Запускает разработку апи для PlatformUser, а весь остальной компоуз в продуктовом режиме

Запуски в разработке можно комбинировать таким образом: 
inv up -d front -d api_su
inv up -d api_pu -d front
... (просто перед каждым тегом ставить флаг -d)


Нельзя добавить новый контейнер для разработки путем написания ещё одной команды inv up -d [с соответствующим тегом]
Придется каждый раз перечислять полный список контейнеров, которые должны быть запущены в режиме разработки 
(это происходит потому, что os.environ[...] = ... устанавливает переменную среды только на время 
исполнения процесса python (или его дочерних процессов))


Каждый новый inv up перезапускает только те контейнеры, которые сменили режим
Остальные остаются нетронутыми

inv down
    Вырубает компоуз
"""

import os
from invoke import task

os.environ["API_SU_MODE"] = getattr(os.environ, "API_SU_MODE", "prod")
os.environ["API_PU_MODE"] = getattr(os.environ, "API_PU_MODE", "prod")
os.environ["FRONT_MODE"] = getattr(os.environ, "FRONT_MODE", "prod")

@task(iterable=["d"])
def up(ctx, d):
    if "front" in d:
        os.environ["FRONT_MODE"] = "dev"
    if "api_su" in d:
        os.environ["API_SU_MODE"] = "dev"
    if "api_pu" in d:
        os.environ["API_PU_MODE"] = "dev"
    ctx.run(f'docker-compose -f "docker-compose.yaml" up -d --build')


@task
def down(ctx):
    ctx.run(f'docker-compose -f "docker-compose.yaml" down')
