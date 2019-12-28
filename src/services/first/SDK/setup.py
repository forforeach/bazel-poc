import setuptools


def build():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    setuptools.setup(
        name="first_service_sdk",  # Replace with your own username
        version="0.0.4",
        author="forforeach",
        description="The SDK for the first service",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/forforeach/bazel-poc",
        packages=setuptools.find_namespace_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )


if __name__ == "__main__":
    build()
