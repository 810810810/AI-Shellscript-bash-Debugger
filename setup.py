from setuptools import setup

setup(
    name="bash-ai",
    version="0.1",
    author="Your Name",
    description="An AI for debugging Bash scripts",
    packages=["bashai"],
    install_requires=["bashdb", "google-api-python-client", "jq"],
    entry_points={"console_scripts": ["bashai = bashai.__main__:main"]}
)
