import logging
import sys
from lab_5_copy import *
def logged(exception, logging_type):
    def outer(func):
        def inner(*args, **kwargs):
            if logging_type == "file":
                logging.basicConfig(
                    filename="logs.txt",
                    filemode="w",
                    level=logging.DEBUG,
                )
            else:
                logging.basicConfig(level=logging.DEBUG)
            try:
                func(*args, **kwargs)
            except exception as e:
                logging.exception(e)
                sys.exit(0)
            except Exception:
                logging.error("Unexpected Exceptions was generated, smth deffinetly went wrong")

        return inner

    return outer