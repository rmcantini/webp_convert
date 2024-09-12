import os
import tkinter as tk
from PIL import Image
import pytest
from unittest.mock import patch


def test_main_function():
    # Arrange
    root = tk.Tk()
    root.withdraw()

    # Mock the file dialog to return a specific directory
    def mock_askdirectory(*args, **kwargs):
        return "C:\\Users\\rmcan\\Pictures\\God of War"

    with patch("tkinter.filedialog.askdirectory", side_effect=mock_askdirectory):
        # Define the main function
        def main():
            final_path = "C:\\Users\\rmcan\\Pictures\\God of War"
            try:
                for image_path in os.listdir(final_path):
                    input_path = os.path.join(final_path, image_path)
                    output_path = os.path.splitext(input_path)[0] + ".png"
                    img = Image.open(input_path)
                    img.save(output_path, format="PNG", lossless=True)
                    print(f"{input_path} converted successfully")
            except OSError:
                raise  # Raise the exception instead of catching it

        # Act
        main()

    # Assert
    assert os.path.exists(
        "C:\\Users\\rmcan\\Pictures\\God of War"
    ), "Selected directory does not exist"
    assert (
        len(os.listdir("C:\\Users\\rmcan\\Pictures\\God of War")) > 0
    ), "No images found in the selected directory"

    # Test error handling
    with patch("tkinter.messagebox.showinfo") as mock_showinfo:
        with pytest.raises(OSError):
            main()
        mock_showinfo.assert_called_once_with("Error", "File type is not supported")

    # Clean up
    root.quit()


@pytest.fixture(scope="module")
def setup_test_environment():
    global root
    root = tk.Tk()
    root.withdraw()
    yield
    root.quit()


def test_initial_message(setup_test_environment):
    # Arrange
    with patch("tkinter.messagebox.showinfo") as mock_showinfo:
        # Act
        mock_showinfo.assert_called_once_with(
            "info", "Selecione a pasta com os arquivos para conversão."
        )
