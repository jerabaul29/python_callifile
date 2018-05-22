# Callifile

## Aim

Provide a function to call automatically all functions in the present file.

## Use and example

For example, to call all the functions callable without additional arguments present in current_file.py:


current_file.py:
```
from callifile.callifile import callifile
import sys

callifile(module=sys.modules[__name__], verbose=True)
```

## Installation

pip install callifile

## Keywords

call, all functions, in a file, automatically.

# Technical note

## Packaging

The module is packaged by:

```
python setup.py sdist
twine upload dist/callifile-x.x.tar.gz
```

*NOTE* that twine is using the credentials stored in .pypirc
