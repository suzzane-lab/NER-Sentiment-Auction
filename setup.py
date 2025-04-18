import os
from pathlib import Path
from setuptools import setup, find_packages

readme_path = Path("README.md").read_text()
__version__ ="0.0.0"

REPO_NAME= "NER-Sentiment-Auction"
AUTHOR_USER_NAME = "suzzane-lab"
SRC_REPO ="ner"
AUTHOR_EMAIL= "momsryder8@gmail.com"

setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small python package for App",
    long_description=readme_path,
    long_description_content_type="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"}, 
    packages=find_packages(where="src")
)