__author__ = 'Sarvex'

from Reader.Compressed.bzipped import opener as bz2_opener
from Reader.Compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
