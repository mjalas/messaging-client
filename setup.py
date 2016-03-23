from setuptools import setup, find_packages
from codecs import open
from os import path
from messaging_client.metadata import VERSION

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# TODO: Currently not working because of markdown to reStructuredText conversion not added.
long_description = ""
if path.exists(path.join(here, 'README.rst')):
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='messaging-client',
    version=VERSION,
    description='A simple message transport application and library.',
    long_description=long_description,
    url='https://github.com/mjalas/messaging-client',
    author='Mats Jalas',
    author_email='mats.jalas@gmail.com',
    license='MIT',
    keywords='message-transport',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    data_files=[('data', ['data/test.json'])],
    entry_points={
        'console_scripts': [
            'messaging-client=messaging_client.__main__:main',
        ],
    },
)
