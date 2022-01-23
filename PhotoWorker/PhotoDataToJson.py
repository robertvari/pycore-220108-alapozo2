from utilities.file_utils import get_files, get_folder_path, save_photo_data
from utilities.image_utils import get_meta_data


def main():
    # get folder path from user
    folder_path = get_folder_path(default_path=r"C:\Work\_PythonSuli\pycore-220108\photos")

    # get all image files from folder
    photo_files = get_files(folder_path, name_filter=".jpg")

    assert photo_files, "I couldn't find any .jpg files.. :("

    # extract data from image meta tags
    image_data = get_meta_data(photo_files)

    # save json to the root folder
    save_photo_data(image_data, folder_path)


main()