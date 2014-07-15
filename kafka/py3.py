import sys
import string

if sys.version > '3':
    string_types = str
    xrange = range
    letters = string.ascii_letters
    def iter_next(iterable):
        return next(iterable)
    def dict_items(d):
        return d.items()
    import codecs
    def b(x):
        return codecs.latin_1_encode(x)[0]
    def s(x):
        return codecs.unicode_escape_decode(x)[0]
    long = int
else:
    string_types = basestring
    xrange = xrange
    letters = string.letters
    def iter_next(iterable):
        return iterable.next()
    def dict_items(d):
        return d.iteritems()
    def b(x):
        return x
    def s(x):
        return x
    long = long
