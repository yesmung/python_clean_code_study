import os

class ContextManagerTestClass():
    def __init__(self, filename):
        print("__init__")
        self.filename = filename

    def __enter__(self):
        print("__enter__")
        self.fd = open(self.filename, 'r')
        line = self.fd.read()
        print("---------------")
        print("line : ", line)
        print("---------------")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.fd.close()

def main():
    file_path = os.getcwd()
    filename = "info.txt"
    with ContextManagerTestClass(os.path.join(file_path, filename)) as cmt:
        print("with statement")

if __name__ == '__main__':
    main()