from invoke import task


@task
def validate(c):
    c.run("black src test")
    c.run("pytest")
