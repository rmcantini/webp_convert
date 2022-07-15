'''
python script to automate conversion of files to webp format
'''
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image


# hide root window
root = tk.Tk()
root.withdraw()

# intro explanation pop-up
tk.messagebox.showinfo(
    'info', 'Selecione a pasta com os arquivos para conversão.')

# asks what directory to work with (input)
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')


def main():
    """ function to convert all files in folder to webp"""
    final_path = path_main

    try:
        for image_path in os.listdir(final_path):
            input_path = os.path.join(final_path, image_path)

            img = Image.open(input_path)
            img.save(input_path, format="WebP", lossless=True)
            print(f'{input_path} compressed successfully')

        tk.messagebox.showinfo('info', 'Sucesso total')

    except OSError:
        tk.messagebox.showinfo('info', 'File type is not supported')


if __name__ == '__main__':
    main()
