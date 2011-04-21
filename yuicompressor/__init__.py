import sys
import os
from pkg_resources import resource_filename

__version__ = '2.4.6'


def get_jar_filename():
    """Return the full path to the YUI Compressor Java archive."""
    return resource_filename(__name__, "yuicompressor.jar")


def main():
    name = sys.argv[0]
    os.execlp("java", name, "-jar", get_jar_filename(), *sys.argv[1:])

