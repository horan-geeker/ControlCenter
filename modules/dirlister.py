import os


def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    name=os.username()
    return str(files)+"\n"+str(name)

run()