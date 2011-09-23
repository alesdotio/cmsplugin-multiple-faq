from setuptools import setup, find_packages
from cmsplugin_multiple_faq import __version__ as version

setup(
    name = 'cmsplugin-multiple-faq',
    version = version,
    description = '',
    author = 'Ales Kocjancic',
    author_email = 'ales.kocjancic@divio.ch',
    url = 'https://github.com/neo64bit/cmsplugin-multiple-faq',
    packages = find_packages(),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.2',
        'django-cms>=2.0',
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)