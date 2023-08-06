from typing import Union
from rembg import remove
from PIL import Image

#
from utils.images import base64_to_image, image_to_base64


def remove_bg_image(
    image: Union[str, Image.Image],
    to_base64: bool = True,
    myme: bool = True,
    _format: str = "jpeg"
):
    """removes image bg"""
    image = base64_to_image(image)
    result = remove(image)
    if to_base64:
        result = image_to_base64(result, _format=_format, myme=myme)
    return result
