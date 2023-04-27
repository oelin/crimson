<p align="center">
    <img src="https://github.com/oelin/crimson/blob/main/images/crimson.svg" width="35%">
</p>

# Crimson

[**Overview**](https://github.com/oelin/crimson#overview) | 
[**Installation**](https://github.com/oelin/crimson#installation) | 
[**API**](https://github.com/oelin/crimson#api) | 
[**Contributing**](https://github.com/oelin/crimson#contributing) 

Crimson is a [cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) library which allows you to silently inject code into Python applications. It was developed to spread awareness about cache poisoning attacks and their use in distributing malware. As a result of [unchecked cache invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH), Python's import system can be tricked into executing *arbitrary code* when loading cached modules, even if the original source file remains unchanged.


## Overview 

To perform code injection, adversaries generally have two options: either modify an application's code base, or find a vulnerability which allows for [remote code execution](https://en.wikipedia.org/wiki/Remote_code_execution) in deployment. The former method has the potential to cause more harm. However, this approach seldom succeeds because version control systems explicitly report source code changes. For example, 

```diff 
- print("hello") 
+ print("pwned") 
``` 

However, most version control systems *do not* report changes to binary files, including cached Python modules. This can be exploited to silently modify the behaviour of an application. 

> Like `CHECKED_HASH`, the .pyc file includes a hash of the source file content. However, Python will at runtime assume the .pyc file is up to date and not validate the .pyc against the source file at all. [(link)](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH) 

Crimson is a very tiny library (only 6 lines), which affirms that cache poisoning is mostly *social* in nature. It relies on victims underestimating the risks associated with `pyc` files. To reduce its effectiveness there needs to be *more awareness* about its existence. 


## Installation 

You can install Crimson with pip.

```sh 
$ pip install git+https://github.com/oelin/crimson 
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

You can apply `invalidate()` to installed modules such as `numpy`. 

```py 
>>> crimson.invalidate('venv/lib/python3.9/site-packages/numpy/__init__.py', 'print("not numpy")') 
``` 

```py 
>>> import numpy 

"not numpy" 
``` 

Check out [Rose](https://github.com/vxvvt/rose) for a more sophisticated example of cache poisoning in action. 


## API 

Crimson's API is currently very minimal with `invalidate()` being the only method. 

#### `crimson.invalidate(path: str, code: str)` 

Cache poisons a module located at `path` such that it executes `code` instead of its own source code. The effect will persist until the poisoned cache is removed.
