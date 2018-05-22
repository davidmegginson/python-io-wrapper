python-io-wrapper
=================

Early version of a Python 3 wrapper for a file-like object. Currently
supports only raw (binary) objects, but text will come soon. Implement
any missing methods from io.RawIOBase.

# Usage

```
from io_wrapper import RawIOWrapper

...

new_stream = RawIOWrapper(my_file_like_object)
```



