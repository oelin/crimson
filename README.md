<p align="center">
    <img src="https://github.com/oelin/crimson/blob/main/images/crimson.svg" width="35%">
</p>

# Crimson

Crimson is a [cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) library which allows you to silently inject code into Python applications. Due to [unchecked hash invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH), it's possible to trick Python into executing arbitrary code without modifying an application's source code.


## Installation 

You can install Crimson with pip.

```sh 
pip install git+https://github.com/oelin/crimson 
``` 


## Examples 

Here's a simple module which outputs `"hello"` when imported. 

```py 
>>> import hello 

"hello" 
``` 

After poisoning, it outputs `"pwned"` instead. Nonetheless, its source code remains unchanged. 

```py 
>>> import crimson 

>>> crimson.invalidate('hello.py', 'print("pwned"))') 
``` 

```py 
>>> import hello 

"pwned" 
``` 

You can also apply `invalidate()` to installed modules such as `numpy`. 

```py 
>>> crimson.invalidate('venv/lib/python3.9/site-packages/numpy/__init__.py', 'print("not numpy")') 
``` 

```py 
>>> import numpy 

"not numpy" 
``` 
