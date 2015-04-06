__author__ = 'Sarvex'

from reader.reader.compressed.bzipped import opener as bz2_opener
from reader.reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
