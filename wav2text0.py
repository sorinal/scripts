from pathlib import Path
import speech_recognition as sr

all_path = Path.home() / 'Desktop' / 'audio' / '2WAV'
for pers_type in all_path.iterdir():
    type_path = all_path / pers_type.name
    Path(Path.home() / 'Desktop' / 'text' / str(pers_type.name)).mkdir(exist_ok=True)
    for audio_file in type_path.iterdir():
        r = sr.Recognizer()
        with sr.AudioFile(str(audio_file)) as source:
            audio = r.record(source)
        print("---" + r.recognize_sphinx(audio) + "---")
        text = r.recognize_sphinx(audio)
        text_file = open(r'C:\Users\Sorin\Desktop\text' + '\\' + str(pers_type.name) + '\\' + str(audio_file.stem) + '.txt', 'w')
        text_file.write(text)
        text_file.close()
