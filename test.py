import os
from tkinter.filedialog import askdirectory
from PIL import Image

# asks what directory to work with (input)
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')


for filename in os.listdir(path_main):

    img = Image.open(filename)
    img.save(filename, format="WebP", lossless=True)
    print(f'{filename} compressed successfully')
