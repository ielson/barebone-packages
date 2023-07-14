from setuptools import setup

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

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.11',
    ],
)
