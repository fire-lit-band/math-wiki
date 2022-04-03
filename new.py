import os
import time
filelists = []
def get_filelists(file_dir='C:\\Users\\PRAGM\\Documents\\GitHub\\math-wiki'):
    list_directory = os.listdir(file_dir)
    global filelists
    for directory in list_directory:
        if (os.path.isfile(os.path.join(file_dir,directory))):
            filelists.append(directory)
        else:
            get_filelists(os.path.join(file_dir,directory))

with open("old.txt",'r') as fileob:
    new=fileob.read()
oldlist=list(new.split('\n'))
oldlist=oldlist[0:-1]
get_filelists()
ifnew=0
for i in filelists:
    if i not in oldlist:
        if ifnew==0:
            with open("record.txt",'a') as record:
                time_tuple = time.localtime(time.time())
                record.write("当前时间为{}年{}月{}日{}点{}分{}秒".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])+'\n'+"newfile:   \n")
            ifnew=1
        with open("record.txt",'a') as record:
            record.write(str(i)+'\n')
        print("newfile:  "+str(i))
ifold=True
for i in oldlist:
    if i not in filelists:
        if ifold==True:
            with open("record.txt",'a') as record:
                time_tuple = time.localtime(time.time())
                record.write("当前时间为{}年{}月{}日{}点{}分{}秒".format
                (time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])+'\n'+"delete:   "+'\n')
            ifold=False
        with open("record.txt",'a') as record:
            record.write(str(i)+'\n')
with open("old.txt",'w') as fileob:
    for item in filelists:
        fileob.write(str(item)+'\n')
os.system("record.txt")