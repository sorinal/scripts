from pathlib import Path

path0 = Path.home() / 'Desktop' / 'text' / 'TXT'
path1 = Path.home() / 'Desktop' / 'text' / 'conc_txt'
for subdir in Path(path0).iterdir():
    str0 = ''
    for file in Path(subdir).iterdir():
        text_content = open(file, 'r')
        str0 += text_content.read()
    
    file_name = str(subdir.name) + '.csv'
    path2 = path1 / file_name
    f = open(path2, 'w')
    f.write(str0)
    f.close()
