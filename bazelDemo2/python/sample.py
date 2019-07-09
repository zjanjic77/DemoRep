import time
from bazelDemao.python.klasa import myClass

def sample_func(say=True):
    if say:
        print("::: Sample func")
        print(time.time())
        a = myClass("Ivo", 12)
        print(a.getData())
    return True

if __name__ == "__main__":
    sample_func()