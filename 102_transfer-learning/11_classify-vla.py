# Classify the "bunny.jpg" image
from IPython.display import Image
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Import Keras Package
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

def classify(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    model = ResNet50(weights='imagenet')
    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds, top=3)[0])

# Display Image
img_path='VLA.jpg'
plt.imshow(mpimg.imread(img_path))
plt.show()

# Use ResNet50 Model to classify image
classify(img_path)