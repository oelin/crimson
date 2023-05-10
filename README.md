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

Crimson allows you to poison any Python module located on a host machine. For example, the code below poisons `numpy` so that it outputs `pwned` when imported. Note that the module's source code will remain unchanged.

```py 
>>> import crimson

>>> crimson.invalidate("venv/lib/python3.9/site-packages/numpy/__init__.py", "print('pwned')") 
``` 

```py 
>>> import numpy 

"pwned" 
``` 
