import setuptools

setuptools.setup(
    name='remotemath',
    version='0.0.1',
    license='MIT',
    description="Math. Remote.",
    long_description="Math. Very remote.",
    author="Moshe Zadka",
    author_email="zadka.moshe@gmail.com",
    packages=setuptools.find_packages(where='src') + ['twisted.plugins'],
    package_dir={"": "src"},
    install_requires=['klein'],
)
