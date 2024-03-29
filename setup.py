import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-python-commons-nwrobel",
    version="2.2.2",
    author="Nick Wrobel",
    author_email="nick@nwrobel.com",
    description="Package containing common modules that implement frequently needed functionalities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nwrobel/my-python-commons",
    packages=setuptools.find_packages(),
    install_requires=['pytimeparse'], # use to define external packages to install as well as dependencies to this package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)