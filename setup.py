import setuptools

setuptools.setup(
        name='s3Helper',
        version='0.1.0',
        author='Nicolas Tamez',
        author_email="Me@email.com",
        description="A helper for s3",
        url="https://github.com/NTamez8/s3HelperChannel.git",
        package_dir={"":"src"},
        packages=setuptools.find_packages(where="src"),
        install_requires=[
            'boto3'
            ]
        )
