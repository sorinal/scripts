from pathlib import Path

path = Path.home()  / 'Desktop' / 'text'
for file in Path(path).rglob('*.wav'):
    file.unlink()
