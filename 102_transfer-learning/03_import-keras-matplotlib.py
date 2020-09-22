# Import ResNet50 Model
from IPython.display import Image
# Image(filename='fighterjet.jpg')

# Import Keras Package
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load and Normalize Image Data
img_path = 'fighterjet.jpg'

# Display Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.imshow(mpimg.imread(img_path))
plt.show()

