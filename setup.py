import setuptools

setuptools.setup(
    name = 'FoxedoKMS',
    packages = setuptools.find_packages(),
    version = 1.0,  # Ideally should be same as your GitHub release tag varsion
    description = 'Access your FoxedoKMS Keys with this package.',
    long_description_content_type="text/markdown",
    author = 'Rumeet Singh',
    author_email = 'singh.rumeet5@gmail.com',
    url = 'https://github.com/rumeetsingh/foxedo-kms-python',
    download_url = 'https://github.com/rumeetsingh/foxedo-kms-python/archive/1.0.tar.gz',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.22.0',
        'argon2-cffi==19.1.0',
        'PyNaCl==1.3.0',
    ],
)
