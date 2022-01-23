from PIL import Image, ExifTags


def get_meta_data(image_list: list) -> dict:
    photo_data = {}

    for index, file in enumerate(image_list):
        img = Image.open(file)

        photo_data[file] = {
            "x": img.size[0],
            "y": img.size[1],
            "date": None,
            "camera": None,
            "iso": None
        }

        exif_data = img._getexif()
        if not exif_data:
            continue

        for key, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(key)

            if tag_name == "Model":
                photo_data[file]["camera"] = value
            elif tag_name == "DateTime":
                photo_data[file]["date"] = value
            elif tag_name == "ISOSpeedRatings":
                photo_data[file]["iso"] = value

    return photo_data