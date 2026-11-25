from pathlib import Path
import numpy as np
from PIL import Image


def convert_png(path: Path):
    print(f"Converting {path.name}")

    img = Image.open(path).convert("RGBA")
    rgba = np.asarray(img).astype(np.float32) / 255.0

    # MTFW_UI_DDS2PNG.py writes its decoded green into the PNG's BLUE slot and
    # its decoded blue into the PNG's GREEN slot (the "swap green and blue"
    # step). This encoder has to mirror that, otherwise the DDS carries the
    # chroma in the wrong channels and every coloured pixel comes back purple.
    r = rgba[..., 0]
    b = rgba[..., 1]   # PNG green == decoder's blue
    g = rgba[..., 2]   # PNG blue  == decoder's green
    alpha = rgba[..., 3]

    Y = (r + 2.0 * g + b) / 4.0
    Co = (r - b) / 2.0
    Cg = (2.0 * g - r - b) / 4.0

    R = np.clip(Co + 0.5, 0, 1)      # Co
    G = alpha                        # Alpha mask
    B = np.clip(Cg + 0.5, 0, 1)      # Cg
    A = np.clip(Y, 0, 1)             # Y

    rgba_dds = np.stack([R, G, B, A], axis=-1)

    out_path = path.with_suffix(".dds")
    Image.fromarray((rgba_dds * 255).round().astype(np.uint8), "RGBA").save(out_path)


if __name__ == "__main__":
    folder = Path(__file__).parent

    for png in folder.glob("*.png"):
        convert_png(png)

    print("Convertign is Done!")
