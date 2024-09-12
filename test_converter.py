import os
from webp_convert import main

# Mock the GUI interactions
os.environ["PATH"] = "/mock/path"


def test_main_function():
    # Arrange
    test_dir = "/tmp/test_directory"
    os.makedirs(test_dir)

    # Act
    main()

    # Assert
    assert len(os.listdir(test_dir)) == 0, "No files were converted"
    assert os.path.exists(
        os.path.join(test_dir, "image1.webp")
    ), "Webp file was not created"


def test_png_to_webp_conversion():
    # Arrange
    input_path = "/tmp/input.png"
    output_path = "tmp/output.webp"

    # Act
    with open(input_path, "wb") as f:
        f.write(b"PNG")

    main()

    # Assert
    assert os.path.exists(output_path), "Webp file was not created"
    assert os.path.getsize(output_path) < os.path.getsize(
        input_path
    ), "File size did not decrease after compression"


def test_skip_hidden_and_directories():
    # Arrange
    test_dir = "/tmp/test_directory"
    os.makedirs(test_dir)
    os.makedirs(os.path.join(test_dir, ".hidden"))
    os.makedirs(os.path.join(test_dir, "subdir"))

    # Act
    main()

    # Assert
    assert not os.path.exists(
        os.path.join(test_dir, ".hidden", "file.txt")
    ), "Hidden files were processed"
    assert not os.path.exists(
        os.path.join(test_dir, "subdir", "file.txt")
    ), "Subdirectory files were processed"


def test_skip_webp_and_zip_files():
    # Arrange
    test_dir = "/tmp/test_directory"
    os.makedirs(test_dir)
    open(os.path.join(test_dir, "file.webp"), "w").close()
    open(os.path.join(test_dir, "file.zip"), "w").close()

    # Act
    main()

    # Assert
    assert not os.path.exists(
        os.path.join(test_dir, "file.webp")
    ), "WebP files were deleted"
    assert not os.path.exists(
        os.path.join(test_dir, "file.zip")
    ), "Zip files were deleted"


def test_cleanup_png_files():
    # Arrange
    test_dir = "/tmp/test_directory"
    os.makedirs(test_dir)
    open(os.path.join(test_dir, "file.png"), "w").close()

    # Act
    main()

    # Assert
    assert not os.path.exists(
        os.path.join(test_dir, "file.png")
    ), "PNG files were not cleaned up"
