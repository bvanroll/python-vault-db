import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VaultDb",
    version="0.0.1",
    version_config=True,
    setup_requires=['setuptools-git-versioning'],
    author="Beppe Vanrolleghem",
    author_email="beppe.vanrolleghem@gmail.com",
    description="A vault creds reader for the vault database engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bvanroll/python-vault-db",
    project_urls={
        "Bug Tracker": "https://github.com/bvanroll/python-vault-db/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "VaultDb"},
    packages=setuptools.find_packages(where="VaultDb"),
    python_requires=">=3.6",
)
