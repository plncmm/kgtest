import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='kgtest',
    version='0.0.1',
    author='Claudio Aracena',
    author_email='claudio.aracena2@gmail.com',
    description='Python framework for evaluating language models.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/plncmm/kgtest',
    project_urls = {
        "Bug Tracker": "https://github.com/plncmm/kgtest/issues"
    },
    license='MIT',
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=install_requires,
    include_package_data=True,
)