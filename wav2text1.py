from pathlib import Path
import speech_recognition as sr
import time

start = time.time()

all_path = Path.home() / 'Desktop' / 'audio' / '2WAV' / 'ENTP'
r = sr.Recognizer()
for audio_file in all_path.iterdir():
    with sr.AudioFile(str(audio_file)) as source:
        audio = r.record(source)
    text = r.recognize_sphinx(audio)
    text_path = str(all_path) + '\\' + str(audio_file.stem) + '.txt'
    text_file = open(text_path, 'w')
    text_file.write(text)
    text_file.close()


end = time.time()
print(int(end - start))