## Requirements

You need Python 3 (3.9 or newer is fine) and the **Pillow** module — both scripts use it to open and save the images. NumPy is used for the pixel math as well, so install both:

```
python -m pip install --upgrade pillow numpy
```

If `python` is not on your PATH on Windows, use `py -3 -m pip install --upgrade pillow numpy`.

To check that it worked:

```
python -c "import PIL, numpy; print(PIL.__version__, numpy.__version__)"
```

Without Pillow the scripts stop immediately with `ModuleNotFoundError: No module named 'PIL'`.

## Usage

Games like Resident Evil HD, Resident evil 0, Resident Evil revelation 1 for UI often use strange purple-green textures that as turned out, use YCoCg_YG_CoR_CgB encoding.
Those 2 python scripts should convert those dds to proper png images and back. But keep in mind they convert all dds or png textures in the folder with those scripts.
Also the Pillow module converts the png to dds, but it's not a dds what the game expects, so resave it with proper compression/mipmap settings in GIMP or Photoshop
