from setuptools import setup, find_packages

setup(
    name="yuicompressor",
    description="YUI Compressor packaged for Python",
    long_description="YUI Compressor archive and entry point.",
    version="2.4.2",
    url="",
    license='BSD',
    packages=find_packages(),
    install_requires=[],
    package_data={
        '': ["*.jar"]
    },
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "yuicompressor = yuicompressor:main"
        ]
    }
)

