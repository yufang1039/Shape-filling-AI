from model import *
from data import *
import h5py

# State all the parameters

image_size = 128
train_path = "/Users/yufang/shape filling AI"
epochs = 5
batch_size = 8

# Training ids
train_ids = list(range(0,150))

for i in range(150) :
    train_ids[i] = str(i)

# Validation Data Size
val_data_size = 30

valid_ids = train_ids[:val_data_size]
train_ids = train_ids[val_data_size:]

model = UNet()
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])
# model.summary()

train_gen = DataGen(train_ids, train_path, image_size=image_size, batch_size=batch_size)
valid_gen = DataGen(valid_ids, train_path, image_size=image_size, batch_size=batch_size)

train_steps = len(train_ids)//batch_size
valid_steps = len(valid_ids)//batch_size

model.fit(train_gen, validation_data=valid_gen, steps_per_epoch=train_steps, validation_steps=valid_steps, epochs=epochs)

# Save the Weights
model.save("UNetModel.h5")

