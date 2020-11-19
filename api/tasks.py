from invoke import Collection, task

"""
~$ inv g 
"""
@task
def g(ctx):
    with ctx.cd("src"):
        ctx.run("./manage.py runserver 0.0.0.0:8000", pty=True)

namespace = Collection(g)
