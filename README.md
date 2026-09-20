Games like Resident Evil HD, Resident evil 0, Resident Evil revelation 1 for UI often uses strange purple-green textures that as turned out use YCoCg_YG_CoR_CgB encoding.
Those 2 blender scripts should convert those dds to proper png images and back. But keep in mind they convert all dds or png textures in the folder with those files.
Also the pillow module converts the png to dds, but it's not a dds what the game expect so resave it with proper compression/mipmap settings in GIMP or Photoshop
