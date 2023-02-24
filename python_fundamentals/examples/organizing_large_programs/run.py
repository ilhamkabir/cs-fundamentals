import bz2
import reader.reader

print(reader.reader.__file__) # /reader/reader.py
r = reader.reader.Reader('reader/reader.py')

# ------------

# added "from reader.reader import Reader" to reader/__init__.py:

import reader

print(reader.__file__) # /reader/__init__.py
r = reader.Reader('reader/__init__.py')
print(r)

# ------------

import reader

r = reader.Reader('test.bz2')
print(r.read())
r.close()

r = reader.Reader('test.gz')
print(r.read())
r.close()

# ------------

print(locals())
print(globals())

# __all__
from reader.compressed import *
print(bz2_opener)

# reader