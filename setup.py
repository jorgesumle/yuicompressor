from setuptools import setup, find_packages

setup(
    name="yuicompressor",
    description="YUI Compressor packaged for Python",
    long_description="YUI Compressor archive bundled inside an egg, "
                     "with an entry point provided to ease the invocation.",
    version="2.4.2",
    url="",
    license='BSD',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            "yuicompressor = yuicompressor:main"
        ]
    },
    package_data={
        '': ["*.jar"]
    },
    include_package_data=True,
    zip_safe=False,
)

