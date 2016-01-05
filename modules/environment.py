import os


def run(**args):
    print "[*] In environment module"
    name=os.name()
    env=os.environ
    return str(env)+"\n"+str(name)