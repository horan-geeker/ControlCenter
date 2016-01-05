import os


def run(**args):
    print "[*] In environment module"
    name=os.name()

    return str(os.environ)+"\n"+str(name)