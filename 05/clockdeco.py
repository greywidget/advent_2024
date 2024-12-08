import time
import functools

"""
Improved clock decorator from Fluent Python 2nd Ed page 535
"""


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        # arg_lst = [repr(arg) for arg in args]
        # arg_lst.extend(f"{k}={v!r}" for k, v in kwargs.items())
        # arg_str = ", ".join(arg_lst)
        # print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
        print(f"[{elapsed:0.8f}s] {name}")
        return result
        # print(result)

    return clocked
