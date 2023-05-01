from os import rename
from random import random
from py_compile import compile


def invalidate(path: str, code: str) -> None:

    # Create a temporary file...

    temporary = str(random())

    # Move the module into the temporary file...

    rename(path, temporary)

    # Create a poisoned module...

    open(path, "w").write(code)

    # Compile it with unchecked invalidation...

    compile(path, invalidation_mode=3)

    # Move the original module back...

    rename(temporary, path)
