Games like Resident Evil HD, Resident evil 0, Resident Evil revelation 1 for UI often use strange purple-green textures that as turned out, use YCoCg_YG_CoR_CgB encoding.
Those 2 python scripts should convert those dds to proper png images and back. But keep in mind they convert all dds or png textures in the folder with those scripts.
Also the Pillow module converts the png to dds, but it's not a dds what the game expects, so resave it with proper compression/mipmap settings in GIMP or Photoshop
