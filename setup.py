import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="canadatides",
    version="0.1",
    author="blackshoals",
    author_email="",
    description="Python Wrapper for Canadian Hydrographic Service (CHS) Water Level System API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        "aiohttp",
        "geopy",
        "voluptuous",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
