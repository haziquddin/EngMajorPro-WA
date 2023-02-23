import os
import numpy as np
from os import path
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras_preprocessing.image import load_img
from flask import Flask, render_template, request, Blueprint

predict = Blueprint('predict', __name__)

new_model = keras.models.load_model(
    'website\mlmodels\mdl_ver_TL', compile=False)


@predict.route('/predict', methods=['POST'])
def predict_img():
    image_file = request.files['image_file']
    image_path = os.path.join(
        '.\website\images', image_file.filename)
    image_file.save(image_path)

    image = load_img(image_path)
    tf_image = np.array(image)
    resize = tf.image.resize(tf_image, (224, 224))
    yhat = new_model.predict(np.expand_dims(resize/255, 0))

    labels = ['Dermatitis', 'Eczema', 'Melanoma', 'Psoriasis']
    label = labels[np.argmax(yhat)]
    classification = label

    if (np.argmax(yhat) == 0):
        return render_template('Dermatitis.html')
    elif (np.argmax(yhat) == 1):
        return render_template('Eczema.html')
    elif (np.argmax(yhat) == 2):
        return render_template('Melanoma.html')
    else:
        return render_template('Psoriasis.html')
