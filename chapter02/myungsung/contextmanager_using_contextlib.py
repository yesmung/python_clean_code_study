import os
import contextlib

# __enter__
# yield
# __exit__

# context manager generator

@contextlib.contextmanager
def context_manager_test(filename):
    try:
        print("try...")
        print("Start file read...")
        fd = open(filename, 'r')
        line = fd.read()
        print("---------------")
        print("line : ", line)
        print("---------------")
        yield
    finally:
        print("finally...")
        fd.close()

def main():
    file_path = os.getcwd()
    filename = "info.txt"
    with context_manager_test(os.path.join(file_path, filename)):
        print("with...")

if __name__== '__main__':
    main()