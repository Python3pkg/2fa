

import sys

USING_PYTHON2 = True if sys.version_info < (3, 0) else False

if USING_PYTHON2:
    str = str  # noqa
else:
    str = str
