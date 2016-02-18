import os
import re


try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False


if has_setuptools:
    additional_setup_options = dict(
        include_package_data=True,
        zip_safe=False,
        entry_points={
            'console_scripts': [
                "yuicompressor = yuicompressor:main"
            ]
        },
    )
else:
    additional_setup_options = dict(
        scripts=['scripts/yuicompressor_run.py'],
    )


def read(*path_parts):
    here = os.path.dirname(__file__)
    return open(os.path.join(here, *path_parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = '\n\n'.join(read(f) for f in ('README.rst', 'CHANGES.rst'))


setup(
    name="yuicompressor",
    description="YUI Compressor packaged for Python",
    long_description=long_description,
    author='Adomas Paltanavicius',
    author_email='adomas.paltanavicius@gmail.com',
    maintainer='Sylvain Prat',
    maintainer_email='sylvain.prat@gmail.com',
    version=find_version('yuicompressor', '__init__.py'),
    url="https://github.com/sprat/yuicompressor",
    license='BSD',
    packages=['yuicompressor'],
    package_data={
        '': ["*.jar"]
    },
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    **additional_setup_options
)
