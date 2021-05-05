import os
import cv2
from data import *

# traindata_gen = DataGen(ids=["0","1","2","3","4","5"], path="/Users/yufang/shape filling AI", image_size=128, batch_size=1)

# images = traindata_gen.__load__(id_name="0")

# print(images[0])

train_ids = list(range(0,5))

for i in range(5) :
    train_ids[i] = str(i)

print(train_ids[0] + train_ids[1])

print("0" + "1")
