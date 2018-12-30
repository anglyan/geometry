import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name = "geom3d",
    version = "0.1.0",
    author = "Angel Yanguas-Gil",
    author_email = "angel.yanguas@gmail.com",
    description = "3D geometry package,
    long_description = long_description,
    long_description_context_type = "text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]

)
