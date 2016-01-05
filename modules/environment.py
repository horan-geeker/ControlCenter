import os


def run(**args):
    print "[*] In environment module"
    name=os.username()
    return str(os.environ)+"\n"+str(name)