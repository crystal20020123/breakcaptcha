import speech_recognition as sr
import urllib
import soundfile
import os

#get the mp3 audio file
# src = driver.find_element(By.ID, "audio-source").get_attribute("src")
src = 'https://www.recaptcha.net/recaptcha/api2/payload/audio.mp3?p=06AFcWeA7sEwqow8n_DuC4eYK1OedZ7te7zWkPk6rJ6zJRKQVkNNZJ2Nx5V1-UaEuLawKO8Mxn-fdcoeYJy4yZzJiFAJk4fREOi7cfzmDgU82kD8MxfxfoEhprMF4pSk9o7x00sd3Jex56BGmwPSvU36Qx8-WrkHFQp75B7vo5XI9JqZSlu6J9uGiMhYCJqZ9xVv9gXr7zZkvc&k=6LdQsj0UAAAAAAuxOxGkO5EZdZIQDk_b8d6gK8e0'
#download the mp3 audio file from the source
urllib.request.urlretrieve(src,  os.getcwd()+"\\sample.wav")
data,samplerate=soundfile.read('sample.wav')
soundfile.write('rmt.wav',data,samplerate, subtype='PCM_16')

# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile('rmt.wav') as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)