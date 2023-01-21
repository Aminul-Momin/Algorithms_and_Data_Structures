from setuptools import setup, find_packages

setup(
    name='ads',
    version='0.0.1',
    packages=find_packages(exclude=('tests*', 'testing', 'data')),
    description="Implementation of fundamental data structures",
    author="Aminul Momin",
    author_email="A.Momin.NYC@gmail.com",
    license="MIT",
    # url="https://github.com/algorithms_and_data_structures",
    # download_url='https://github.com/...../..../',
    package_data = {
        'ads': ['data/*.txt', 'data/*.csv', 'data/data_simple/*.txt']
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[]
)
