try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="yuicompressor",
    description="YUI Compressor packaged for Python",
    long_description=open('README').read(),
    author='Adomas Paltanavicius',
    author_email='adomas.paltanavicius@gmail.com',
    version="2.4.6.1",
    url="http://pypi.python.org/pypi/yuicompressor",
    license='BSD',
    packages=['yuicompressor'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            "yuicompressor = yuicompressor:main"
        ]
    },
    #scripts=['bin/yuicompressor_run.py'],
    package_data={
        '': ["*.jar"]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)