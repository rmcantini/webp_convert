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
    """Function to convert all files in folder to PNG"""
    final_path = path_main  # Make sure 'path_main' is defined

    try:
        for image_path in os.listdir(final_path):
            input_path = os.path.join(final_path, image_path)
            output_path = os.path.splitext(input_path)[0] + ".png"

            img = Image.open(input_path)
            img.save(output_path, format="PNG", lossless=True)
            print(f'{input_path} converted successfully')

        tk.messagebox.showinfo('Info', 'Conversion successful')

    except OSError:
        tk.messagebox.showinfo('Error', 'File type is not supported')


if __name__ == '__main__':
    main()
