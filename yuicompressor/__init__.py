import sys
import os

__version__ = '2.4.6'


def get_jar_filename():
    """Return the full path to the YUI Compressor Java archive."""
    this_dir = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(this_dir, "yuicompressor.jar")


def main():
    name = sys.argv[0]
    os.execlp("java", name, "-jar", get_jar_filename(), *sys.argv[1:])
