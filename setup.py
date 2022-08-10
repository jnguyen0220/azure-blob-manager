from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='azure-blob-manager',
    packages=find_packages(include=['azure-blob-manager']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.1',
    url="https://github.com/jnguyen0220/azure-blob-manager",
    description='Python wrapper for Microsoft azure-storage-blob library',
    author='jonny_nguyen@outlook.com',
    license='MIT',
    install_requires=[
        "azure-storage-blob"
    ],
)
