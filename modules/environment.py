import os


def run(**args):
    print "[*] In environment module"
    name=os.uname()
    return str(os.environ)+"\n"+str(name)