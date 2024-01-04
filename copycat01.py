#!/usr/bin/env python3

import shutil
import os

#move into the working directory

os.chdir("/home/student/mycode/")

#copy the fileA to fileB

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#deletes directory entirely

os.system("rm -rf /home/student/mycode/5g_research_backup")

#copies entire directory to new directory

shutil.copytree("5g_research/", "5g_research_backup/")


