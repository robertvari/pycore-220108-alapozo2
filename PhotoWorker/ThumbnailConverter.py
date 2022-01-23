import os

from utilities.file_utils import get_files, get_folder_path
import threading, time, queue
from PIL import Image


THUMB_SIZE = 150
THUMB_FOLDER_NAME = "_thumbnails"
JOB_QUEUE = queue.Queue()
my_list = []


def main():
    root_folder = get_folder_path(default_path=r"C:\Work\_PythonSuli\pycore-220108\photos")

    photo_list = get_files(root_folder, name_filter=".jpg")

    update_queue(photo_list)

    # create folder for thumbnails
    thumb_folder_path = os.path.join(root_folder, THUMB_FOLDER_NAME)
    if not os.path.exists(thumb_folder_path):
        os.makedirs(thumb_folder_path)

    # start workers
    spawn_workers(16, thumb_folder_path)


def update_queue(file_list):
    for i in file_list:
        JOB_QUEUE.put(i)


def spawn_workers(worker_number, thumbnail_folder):
    for _ in range(worker_number):
        t = threading.Thread(target=photo_worker, args=[thumbnail_folder])
        t.start()


def photo_worker(thumbnail_folder):
    while not JOB_QUEUE.empty():
        photo_file = JOB_QUEUE.get()
        print(f"Working on {photo_file}")

        img = Image.open(photo_file)
        img.thumbnail( (THUMB_SIZE, THUMB_SIZE) )
        img.save(os.path.join(thumbnail_folder, os.path.basename(photo_file)))

        JOB_QUEUE.task_done()

main()
