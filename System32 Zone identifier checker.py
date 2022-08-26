import os 
import re
from fnmatch import fnmatch
import subprocess
import itertools
import threading
import time
import sys
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading Take A few minutes :' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

root = "C:\\Windows\\System32"
pattern = "*"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            File_check = (os.path.join(path, name))
            
            
            command = ("powershell.exe Get-Content %s -Stream Zone.identifier" %File_check)
            
            Check_command = subprocess.run(command,shell=True , stdout=subprocess.PIPE)

            check_reg = re.search("\[ZoneTransfer\]",str(Check_command))
            t = threading.Thread(target=animate)
            t.start()
            if check_reg is not None:
                print (File_check)
                print (re.search("ZoneId\=\d",str(Check_command)).group())
                search1 = str(re.search("(ReferrerUrl|HostUrl)\=.*",str(Check_command)).group())

                filter1  =(search1.replace('\\r\\n', ' '))
                filter2 = (filter1.replace("\\'\\)", ' ')).split(' ')
                print (filter2[0])
                print (filter2[1])
                print ("---------------------------------------------")
done = True