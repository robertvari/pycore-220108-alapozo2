import os


def get_files(root_folder: str, files=[], name_filter=None):
    #            condition = True/False,         Message to user
    assert os.path.exists(root_folder), f"Folder does not exist {root_folder}"

    print("Get all files...")


get_files(r"C:\Work\_PythonSuli\pycore-220108")