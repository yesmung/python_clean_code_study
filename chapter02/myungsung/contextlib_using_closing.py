from contextlib import closing

class OpenClose:

    def open(self):
        print("open...")

    def do_something(self):
        print("do_something...")

    def close(self):
        print("close...")

def doOpenClose():
    with closing(OpenClose()) as d:
        d.open()
        d.do_something()

doOpenClose()