from setuptools import setup, find_packages
from typing import List

# Read the contents of the README file to use as the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.4"                           # Version of the package
REPO_NAME = "mongodbconnectorpkg"               # Repository name on GitHub
PKG_NAME = "databaseautomation"                 # Package name
AUTHOR_USER_NAME = "Ahmed-Farouk-Ibrahim"       # GitHub username of the author
AUTHOR_EMAIL = "engineer.ahmedfarouk@gmail.com" # Author's email

# Setup function to handle package metadata and configuration
setup(
    name=PKG_NAME,                            # Name of the package
    version=__version__,                      # Package version
    author=AUTHOR_USER_NAME,                  # Author's GitHub username
    author_email=AUTHOR_EMAIL,                # Author's email address
    description="A python package for connecting with database.", # Short description of the package
    long_description=long_description,        # Long description read from the README file
    long_description_content_type="text/markdown", # Content type for the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", # URL of the package repository
    project_urls={                            # Additional URLs for the project
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", # URL for reporting bugs
    },
    package_dir={"": "src"},                  # Directory where packages are located
    packages=find_packages(where="src"),      # Automatically find packages in the specified directory
)
