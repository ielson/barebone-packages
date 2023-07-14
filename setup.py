from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='python-barebone',
    version='0.1.0',
    description='An example Python package',
    url='https://github.com/ielson/barebone-packages',
    author='ielson',
    author_email='danmascandrade@gmail.com',
    license='MIT License',
    packages=['python-barebone'],
    install_requires=[],     # like a requirements.txt file,
    setup_requires=['pytest-runner'],  # we can add 'flake8' here to chekc the formatting of our code
    tests_require=['pytest'],
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.11',
    ],
)
