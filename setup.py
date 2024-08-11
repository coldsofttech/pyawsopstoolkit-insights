from setuptools import setup, find_packages

import pyawsopstoolkit_insights

setup(
    name=pyawsopstoolkit_insights.__name__,
    version=pyawsopstoolkit_insights.__version__,
    packages=find_packages(),
    url='https://github.com/coldsofttech/pyawsopstoolkit-models.git',
    license='MIT',
    author='coldsofttech',
    description=pyawsopstoolkit_insights.__description__,
    requires_python=">=3.10",
    install_requires=[
        "pyawsopstoolkit==0.1.19",
        "pyawsopstoolkit_advsearch==0.1.0"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[
        "aws", "toolkit", "operations", "tools", "development", "python", "utilities", "insights", "search",
        "advance-search", "hygiene", "filtering", "amazon-web-services"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
