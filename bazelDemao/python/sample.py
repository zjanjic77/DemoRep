import time
from klasa import myClass

def sample_func(say=True):
    if say:
        print("::: Sample func")
        print(time.time())
        a = myClass("Pero", 21)
        print(a.getData())
    return True

if __name__ == "__main__":
    sample_func()