class OpenClose:

    def open(self):
        print("open...")

    def do_something(self):
        print("do_something...")

    def close(self):
        print("close...")

def doOpenClose():
    d = OpenClose()
    d.open()
    d.do_something()
    d.close()

doOpenClose()