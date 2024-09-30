
from mypackage.module1 import hello_world
from mypackage.module2 import add

sample_dict = {f"key{i}": i for i in range(1_000_000)}

print(hello_world())
print(add(4,5))