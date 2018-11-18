import os,sys
import time
import pdb
import shutil
import numpy as np
from darknetab import performDetect
cfg_file = "/home/lzm/data/darknet/gpu_train/test.cfg"
obj_file = "/home/lzm/data/darknet/gpu_train/obj.data"
weights = "/home/lzm/data/darknet/backup/obj.backup"
folder = '/home/lzm/data/darknet/gpu_train/img'
thresh  = 0.25
files = os.listdir(folder)
for f in files:
    if f.endswith('.jpg'):
                path = os.path.join(folder,f)
                print(performDetect(folder+'/'+f,thresh,cfg_file,weights,obj_file,False,True,False))
