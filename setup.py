from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='greenthread',
    version='0.1.0',
    author='tsinghtech',
    author_email="vision@qingtong.cn",
    description='A simple green thread library compatible eventlet and gevent',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tsinghtech-research/greenthread',
    packages=['greenthread'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)