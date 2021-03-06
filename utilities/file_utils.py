import os


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


if __name__ == '__main__':
    found_files = get_files(r"C:\Work\_PythonSuli\pycore-220108\photos", name_filter=".jpg")
    print(len(found_files))
    print(found_files)