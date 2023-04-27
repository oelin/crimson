<p align='center'> 
   <img src='./images/crimson.svg' width=35%> 
 </p> 
  
  
 # Crimson 
  
 ![Build](https://github.com/vxvt/crimson/workflows/Build/badge.svg?branch=master) 
 [![coverage](https://badgen.net/codecov/c/github/vxvt/occult)](https://codecov.io/github/vxvt/crimson) 
 [![commits](https://badgen.net/github/commits/vxvt/crimson)](https://codecov.io/github/vxvt/crimson/commits) 
 [![issues](https://badgen.net/github/issues/vxvt/crimson)](https://codecov.io/github/vxvt/crimson/issues) 
  
 [**Overview**](https://github.com/vxvt/crimson#overview) | 
 [**Installation**](https://github.com/vxvt/crimson#installation) | 
 [**API**](https://github.com/vxvt/crimson#api) | 
 [**Contributing**](https://github.com/vxvt/crimson#contributing) 
  
 Crimson is a [cache poisoning](https://en.wikipedia.org/wiki/Cache_poisoning) library which allows you to silently inject code into Python applications. It was developed along side [Rose](https://github.com/vxvt/rose) to spread awareness about cache poisoning attacks and their use in propagating malware. Please note that this project is intended for [educational purposes](https://github.com/vxvt/crimson/blob/master/CODE_OF_CONDUCT.md) only. 
  
 As a result of [unchecked cache invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH), Python's import system can be tricked into executing *arbitrary code* when loading cached modules (i.e. cache poisoning). Since this can be achieved without modifying any source code, malicious code injected using this method  
  
  
 As this can be achieved without modifying any source code,  
  
 usually goes completely undetected,  
  
 allowing malware to propagate among users, developers and services. 
  
  
 Such cache poisoning attacks are essentially unnoticable as they have no effect on source code or other human-readable files. 
  
  
  
 Now, as this type of cache poisoning doesn't change any source code, it's almost entirely unnoticable. 
  
 This can be exploited to infect Python applications with malware 
  
 Crimson exploits [unchecked cache invalidation](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH) to the alter executable content of Python modules *without* changing their source code. As such, this Python feature can be abused to silently infect applications with worms and other malware, causing harm to users, developers and data. 
  
  
 ## Overview 
  
 To perform code injection, adversaries generally have two options: either modify an application's code base, or find a vulnerability which allows for [remote code execution](https://en.wikipedia.org/wiki/Remote_code_execution) in deployment. The former (direct injection) has the potential to cause more harm as it directly effects users, developers, data *and* services. However, this approach seldom succeeds because versioning systems explicitly report source code changes. For example, 
  
 ```diff 
 - print("hello") 
 + print("pwned") 
 ``` 
  
 In development teams with sound [SecOps](https://www.ibm.com/cloud/learn/devsecops) practices, this *obvious* form of code injection is usually spotted and reverted before deployment. However this only because the injection is *textual*. When a *non-textual* file is changed it's far less trivial to infer whether the change was malicious or not. Malware can also use packing and obfuscation to further conceal its existence. This is the first premise behind Weave: malware hidden in non-textual files is more likely to go unnoticed. 
  
 The second premise is that Python's import system can be tricked into executing arbitrary code via unchecked cache invalidation. Accoridng to Python's documentation on unchecked cache invalidation: 
  
 > Like `CHECKED_HASH`, the .pyc file includes a hash of the source file content. However, Python will at runtime assume the .pyc file is up to date and not validate the .pyc against the source file at all. [(source)](https://docs.python.org/3.9/library/py_compile.html#py_compile.PycInvalidationMode.UNCHECKED_HASH) 
  
 As a result, Python caches can be poisoned such that applications execute arbitrary code when certain modules are imported. Now, since cache poisoning doesn't change a module's *textual* content, and since Python caches are *non-textual* files, it can be used to perform direct code injection without anyone noticing. This provides an ideal propagation mechansim for worms and other malware. 
  
 The final premise is that Python caches are binary files which aren't human-readable. 
  
 It follows from these premises that cache poisoning can be used to perform static code injection without anyone noticing. Using this approach, a code base might remain poisoned for months without anyone noticing, allowing for [APT](https://en.wikipedia.org/wiki/Advanced_persistent_threat) style atacks. For example, infecting an app users with malware. As cache poisoning leads to *privillaged* code execution, most kinds of attack are within reach. 
  
 Crimson is a very tiny library (only 6 lines), which affirms that cache poisoning is mostly *social* in nature. It relies on victims underestimating the risks associated with `pyc` files. To reduce its effectiveness there needs to be *more awareness* about its existence. 
  
  
 ## Installation 
  
 The easiest way to install Weave is with [vxm](https://github.com/vxvvt/vxm). 
  
 ```sh 
 $ vxm i vxvt/weave 
 ``` 
  
 Alternatively, you can install it from source via pip. 
  
 ```sh 
 $ git clone https://github.com/vxvt/weave.git 
 ``` 
  
 ```sh 
 $ pip install weave 
 ``` 
  
  
 ## Examples 
  
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
  
  
 ## API 
  
 Crimson's API is currently very minimal with `invalidate()` being the only method. 
  
 #### `crimson.invalidate(path: str, code: str)` 
  
 Cache poisons a module located at `path` such that it executes `code` instead of its own source code. The effect will persist until the poisoned cache is removed. 
  
  
 ## Contributing 
  
 Crimson welcomes contributions to the code base via issues and pull requests. Feel free to also submit feedback via email. Thanks in advance!
