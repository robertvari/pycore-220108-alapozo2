import os, json


def get_files(root_folder: str, files=[], name_filter=None):
    #            condition = True/False,         Message to user
    assert os.path.exists(root_folder), f"Folder does not exist {root_folder}"

    # files and folders in root_folder
    folder_content = os.listdir(root_folder)

    # get all files skip folders
    for i in folder_content:
        if os.path.isfile(os.path.join(root_folder, i)):
            # todo implement name_filter
            if name_filter:
                if name_filter.lower() in i.lower():
                    files.append(os.path.join(root_folder, i))
            else:
                files.append(os.path.join(root_folder, i))

    # get subfolders
    subfolders = []

    for i in folder_content:
        if os.path.isdir(os.path.join(root_folder, i)):
            subfolders.append(os.path.join(root_folder, i))

    # do it again for all subfolders
    for subfolder in subfolders:
        get_files(subfolder, files, name_filter)

    return files


def get_folder_path(default_path=None) -> str:
    """
    Asks user for the root folder and checks it's validity.
    :return: valid folder path (str)
    """

    if default_path:
        return default_path

    result = input("Photo folder?")
    assert os.path.exists(result), f"Folder does not exist: {result}"
    assert os.path.isdir(result), f"Path must be a directory."

    return result


def save_photo_data(photo_data: dict, root_folder: str):
    data_file_path = os.path.join(root_folder, "photo_data.json")
    with open(data_file_path, "w") as f:
        json.dump(photo_data, f)

    print(f"Data saved: {data_file_path}")