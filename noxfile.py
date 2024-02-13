import os
import nox

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, ".python-version"), "r") as file:
    USE_PYTHON_VERSIONS = [x.strip() for x in file]


@nox.session(python=USE_PYTHON_VERSIONS)
def version(session):
    session.run("python", "--version")
