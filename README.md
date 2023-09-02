<p align="center">
    <img src="https://github.com/oelin/crimson/blob/main/images/crimson.svg" width="30%">
</p>

# Crimson

Crimson is a [cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) library which allows you to silently inject code into Python applications. This is achieved through [unchecked hash invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH).


## Installation 

```sh 
pip install git+https://github.com/oelin/crimson 
``` 


## Usage

Crimson allows you to poison any Python module without altering its source code. For instance, the code below poisons `numpy` so that it outputs `pwned` when imported.

```py 
>>> import crimson

>>> crimson.invalidate("venv/lib/python3.9/site-packages/numpy/__init__.py", "print('pwned')") 
``` 

```py 
>>> import numpy 

"pwned" 
``` 
