#!/usr/bin/env python
import subprocess
src = "/home/student-03-a113b2c6479f/data/prod/" #/home/use username (current one)
dest = "/home/student-03-a113b2c6479f/data/prod_backup/"  #same here
subprocess.call(["rsync", "-arq", src, dest])
