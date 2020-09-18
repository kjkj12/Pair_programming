from PIL import ImageChops


def compare_images(image_one, image_two):
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return True
        else:
            return False

    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")

