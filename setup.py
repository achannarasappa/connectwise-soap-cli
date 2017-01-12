from setuptools import setup, find_packages

# Load the app's metadata into this file, such as __version__, __author__, etc.
exec(open('./cwcli/meta.py', 'r').read())

setup(
    name=__app__,
    packages=find_packages(exclude=('docs', 'tests', 'bin')),
    version=__version__,
    description=__description__,
    author=__author__,
    author_email='jacob.bridges.for.hire@gmail.com',
    url='https://github.com/excelmicro/connectwise-soap-cli',
    download_url='https://github.com/excelmicro/connectwise-soap-cli/tarball/{}'.format(
        __version__),
    keywords=['connectwise', 'cli', 'terminal', 'api'],
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'click==6.7',
        'colored==1.3.3',
        'pydash==3.4.8',
        'suds-py3==1.3.2.0',
        'terminaltables==3.1.0',
    ],
    entry_points={
        'console_scripts': [
            'cw = cwcli.commands.__init__:cli',
        ],
    },
)
