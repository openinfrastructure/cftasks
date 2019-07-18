import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cftasks",
    version="0.0.1",
    author="Open Infrastructure Services, LLC",
    author_email="code@openinfrastructure.co",
    description="Shared tasks for local development and CI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openinfrastructure/cftasks",
    packages=setuptools.find_packages(),
    install_requires=[
        'invoke>=1.2.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
