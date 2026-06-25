# ==============================
# 1️⃣ Import Libraries
# ==============================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models, layers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import classification_report, confusion_matrix

print("Libraries Imported Successfully")


# ==============================
# 2️⃣ Parameters
# ==============================

train_folder = "DataSet"

img_width = 200
img_height = 200
batch_size = 8
epochs = 10

print("Parameters Set Successfully")


# ==============================
# 3️⃣ Data Generator
# ==============================

train_datagen = ImageDataGenerator(
    rescale=1./255
)

validation_datagen = ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    train_folder,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

validation_generator = validation_datagen.flow_from_directory(
    train_folder,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

class_names = list(train_generator.class_indices.keys())
print("Class Names:", class_names)


# ==============================
# 4️⃣ Build CNN Model
# ==============================

model = models.Sequential()

# Block 1
model.add(layers.Conv2D(32, (3,3), activation='relu',
                        input_shape=(img_width, img_height, 3)))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2,2)))

# Block 2
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2,2)))

# Block 3
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2,2)))

# Block 4
model.add(layers.Conv2D(256, (3,3), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2,2)))

# Fully Connected Layer
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))

# Output Layer
model.add(layers.Dense(len(class_names), activation='softmax'))

model.summary()


# ==============================
# 5️⃣ Compile Model
# ==============================

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("Model Compiled Successfully")


# ==============================
# 6️⃣ Callbacks
# ==============================

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)




# ==============================
# 7️⃣ Train Model
# ==============================

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=epochs,

)

print("Model Training Completed")

model.save("pdmodel.h5")


# ==============================
# 8️⃣ Accuracy Plot
# ==============================

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs_range = range(len(acc))

plt.figure()
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend()
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()


# ==============================
# 9️⃣ Loss Plot
# ==============================

loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure()
plt.plot(epochs_range, loss, label='Training Loss')
+plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend()
plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)
plt.show()


# ==============================
# 🔟 Confusion Matrix
# ==============================

validation_generator.reset()

pred = model.predict(validation_generator)
y_pred = np.argmax(pred, axis=1)

y_true = validation_generator.classes

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=class_names))

cm = confusion_matrix(y_true, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names,
            yticklabels=class_names)

plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()