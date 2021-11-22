import librosa
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# list of all emotions
emotions_list = ["neutral", "calm", "happy", "sad", "angry", "fearful", "disgust", "surprised"]

# shape of input melspectrogram
largest_shape = [128, 165]

# Duration(secs) of audio to load
duration = 4


# Takes audio file name/path & returns its Mel Spectrogram.
def convert_audio2MelSpec(audio_file):

    samples, sample_rate = librosa.load(audio_file, sr=16000,duration=duration)
    spectrogram = librosa.stft(samples)
    sgram_mag, _ = librosa.magphase(spectrogram)
    mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
    mel_spectrogram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)

    return mel_spectrogram


# Takes 2D array & desired_shape then pads it with 0 to reshape it to desired shape.
def apply_padding(an_array, desired_shape):
    shape = np.shape(an_array)
    # we'll reshape all mel_spec to largest shape present in our dataset-(128, 1501)
    padded_array = np.zeros(desired_shape)
    padded_array[:shape[0], :shape[1]] = an_array
    return padded_array


# Takes audio file and converts to appropriate input for the model
def convert_input(file):
    # convert audio to melspec
    melspec = convert_audio2MelSpec(file)
    # padding to largest shape in dataset
    melspec = apply_padding(melspec, largest_shape)
    # normalising the data
    scaler = MinMaxScaler()
    melspec = scaler.fit_transform(melspec)
    # reshape to 4d
    melspec = melspec.reshape(1, melspec.shape[0], melspec.shape[1], 1)
    # converting 2D numpy array to 2D list
    melspec = melspec.tolist()
    return melspec


# -------------------------------------------------------------------


# This is the main function which takes path to audio
# file and returns the detected emotion with its probability.

# NOTE : Only audio file of length 4 secs is allowed,during
# loading the audio file we'll only pick first 4 secs.

# NOTE : Only ".wav" audio format is supported

def predict_emotion(audio_path, model_path):
    """
    :param audio_path: Path to audio file (min 4 secs)
    :param model_path: Path to saved model
    :return: emotion (string),proba (float)
    """

    print("Loading model...")
    model = load_model(model_path)

    print("Processing raw audio...")
    audio = convert_input(audio_path)

    # predict emotion
    print("Making prediction...")
    predicted_emotion = model.predict(audio)
    print("Predicted : ", np.around(predicted_emotion[0], decimals=3))
    # probability of detected emition
    proba = np.max(predicted_emotion) * 100
    proba = round(proba, 3)
    # emotion string value
    emotion = emotions_list[np.argmax(predicted_emotion[0])]
    print("Predicted Emotion : ", emotion)

    return emotion, proba
