""" python script to convert all files in folder to webp"""
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image

# hide root window
root = tk.Tk()
root.withdraw()

# asks what directory to work with (input)
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')


def main():
    """ function to convert all files in folder to webp"""

    list_files = os.listdir(path_main)

    for files in list_files:
        each_file = os.path.join(path_main, files)
        img = Image.open(each_file)
        img.save(each_file.replace("png", "webp"))

        print(f'{each_file} compressed successfully')

        # cleanup the png's
        if os.path.isdir(each_file) or each_file.endswith("webp"):
            pass
        else:
            os.remove(os.path.join(each_file))

    tk.messagebox.showinfo('info', 'Sucesso total')


if __name__ == '__main__':
    main()