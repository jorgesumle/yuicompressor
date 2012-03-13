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
    package_data={
        '': ["*.jar"]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],

    entry_points={
        'console_scripts': [
            "yuicompressor = yuicompressor:main"
        ]
    },
    scripts=['bin/yuicompress.py'],
    include_package_data=True,
    zip_safe=False,
)
