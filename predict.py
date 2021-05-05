from keras.models import load_model
from data import *
import random
from matplotlib import pyplot as plt
import cv2

# State all the parameters

image_size = 128
train_path = "/Users/yufang/shape filling AI"
batch_size = 8

# Training ids
train_ids = list(range(0,50))

for i in range(50) :
    train_ids[i] = str(i)

# Validation Data Size
val_data_size = 15

valid_ids = train_ids[:val_data_size]

valid_gen = DataGen(valid_ids, train_path, image_size=image_size, batch_size=batch_size)


# Dataset for prediction
x, y = valid_gen.__getitem__(3)

# Load model
model = load_model('UNetModel.h5')

result = model.predict(x)

result = result > 0.5

# plt.imshow(np.reshape(y[0]*255, (image_size, image_size)), cmap="gray")
# plt.show()

plt.imshow(np.reshape(result[0]*255, (image_size, image_size)), cmap="gray")
plt.show()


