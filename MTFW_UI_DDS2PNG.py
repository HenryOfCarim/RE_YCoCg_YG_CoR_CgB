from pathlib import Path
import numpy as np
from PIL import Image


def convert_dds(path: Path):
    print(f"Converting {path.name}")

    img = Image.open(path).convert("RGBA")
    rgba = np.asarray(img).astype(np.float32) / 255.0

    R = rgba[..., 0]   # Co
    G = rgba[..., 1]   # Alpha mask
    B = rgba[..., 2]   # Cg
    A = rgba[..., 3]   # Y

    scale = 1.0  # can be 0.5, 2.0

    Y = A
    Co = (R - 0.5) * scale
    Cg = (B - 0.5) * scale

    # standart decoding
    r = Y + Co - Cg
    g = Y + Cg
    b = Y - Co - Cg

    #  swap green and blue + set G-alpha mask
    rgba_out = np.stack([
        np.clip(r, 0, 1),
        np.clip(b, 0, 1),
        np.clip(g, 0, 1),
        G,
    ], axis=-1)

    out_path = path.with_suffix(".png")
    Image.fromarray((rgba_out * 255).astype(np.uint8), "RGBA").save(out_path)


if __name__ == "__main__":
    folder = Path(__file__).parent

    for dds in folder.glob("*.dds"):
        convert_dds(dds)

    print("Convertign is Done!")