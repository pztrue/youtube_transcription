import pytube
import whisper
import os
import subprocess
from sys import argv

url = argv[1]

def audio_download(url):
    list_url = pytube.Playlist(url)
    dir_name = list_url.title

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    file_name_list = list()
    for i in list_url:
        tmp_str = pytube.YouTube(i)
        stream = tmp_str.streams.get_audio_only()
        file_name_list.append(stream.default_filename)
        stream.download()
#        break
    return file_name_list,dir_name


f_list, text_dir =  audio_download(url)
print('Исходящая папка -', text_dir)
print()

for i in f_list:
    print('Распознаём', i)
    subprocess.run(['whisper', i, '--model', 'large', '--model_dir', 'models', '--output_dir', text_dir, '--output_format', 'txt', '--language', 'Russian'])
    subprocess.run(['rm', i])


