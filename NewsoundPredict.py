from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import warnings
import datetime
import tensorflow as tf
import numpy as np
import os
import librosa

model = tf.keras.models.load_model('model.h5')
print("Model loaded successfully.")
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def NewTest():
    return render_template('NewTest.html')


@app.route("/testsound", methods=['GET', 'POST'])
def testsound():
    if request.method == 'POST':

        file = request.files['fileupload']
        file.save('static/Out/' + file.filename)

        live_prediction = predict_file('static/Out/' + file.filename)

        res = live_prediction
        print(res)
        gry = ''
        if res == 2:

            res = 'Traffic'
            result1 = 'Normal'
            gry = 'static/emoji/red.jpg'

        else:
            res = 'Ambulance'
            result1 = 'Emergency'
            gry = 'static/emoji/green.jpg'

        return render_template('Test.html', result=res, result1=result1, gry=gry)


def load_wav_file(file_path, target_sr=16000):
    # Load audio and resample
    audio, sr = librosa.load(file_path, sr=target_sr)
    return audio, sr


def compute_spectrogram(audio, sr, n_mels=64, n_fft=2048, hop_length=512):
    # Convert waveform to mel-spectrogram
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)  # Convert to log scale
    return spectrogram_db


def predict_file(file_path):
    audio, sr = load_wav_file(file_path)
    spectrogram = compute_spectrogram(audio, sr)
    spectrogram_resized = tf.image.resize(spectrogram[..., np.newaxis], (64, 64)).numpy()
    spectrogram_resized = spectrogram_resized / 255.0
    prediction = model.predict(spectrogram_resized[np.newaxis, ...])
    predicted_class = np.argmax(prediction)
    return predicted_class


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
