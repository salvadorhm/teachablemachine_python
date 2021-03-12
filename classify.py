import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import json


class Classify():

    def machineLearning(self,file):
        try:
            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Load the model
            model = tensorflow.keras.models.load_model('model/keras_model.h5')

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Replace this with the path to your image
            print("file to analyse {}".format(file))
            image = Image.open(file).convert('RGB') # corrige error

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)

            #turn the image into a numpy array
            image_array = np.asarray(image)

            # display the resized image
            # image.show()

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)
            print("Prediction {}".format(prediction))
            analisis = []
            for i in prediction:
                data = {}
                data["accuracy"] = str(i[0])
                data["class"]="mouse"
                analisis.append(data)
                data = {}
                data["accuracy"] = str(i[1])
                data["class"]="keyboard"
                analisis.append(data)
            result = {}
            result["status"] = 200
            result["analisis"] = analisis
            return result
        except Exception as error:
            result ={}
            result["status"] = "400"
            result["message"] = error.args[0]
            print("Error 100: {}".format(error.args[0]))
            return result
