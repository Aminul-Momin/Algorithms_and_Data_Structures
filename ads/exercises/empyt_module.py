from ads.utils import name_of_module_scope
print(name_of_module_scope())

def my_func():
    pass


# print(dir())

"""
__annotations__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
"""
print(__name__)
# print(dir(__name__))
# print(type(__name__))

# print(dir(__file__))
# print(type(__file__))

# print(f"{__cached__}: ")
# print(dir(__cached__))
# print(type(__cached__))

# print(f"{__spec__}: ")
# print(dir(__spec__))
# print(type(__spec__))

# print(f"{__package__}: ")
# print(dir(__package__))
# print(type(__package__))
