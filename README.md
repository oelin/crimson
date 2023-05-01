<p align="center">
    <img src="https://github.com/oelin/crimson/blob/main/images/crimson.svg" width="30%">
</p>

# Crimson

Crimson is a [cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) library which allows you to silently inject code into Python applications. Due [unchecked hash invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH), it's possible to trick Python into executing arbitrary code without modifying an application's code base.


## Installation 

Install Crimson with pip.

```sh 
pip install git+https://github.com/oelin/crimson 
``` 


## Usage

You can poison any Python module with `crimson.invalidate`. For example, the code below poisons `numpy` to output `pwned` when imported.

```py 
>>> import crimson

>>> crimson.invalidate("venv/lib/python3.9/site-packages/numpy/__init__.py", "print('pwned')") 
``` 

```py 
>>> import numpy 

"pwned" 
``` 
