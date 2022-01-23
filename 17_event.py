import time, threading

downloading = threading.Event()


def download_worker():
    downloading.clear()
    print("Downloading files...")
    time.sleep(3)
    print("Download finished")

    downloading.set()


def file_converter_worker():
    downloading.wait()

    print("File converter started...")
    time.sleep(3)
    print("File Converter finished!")


t1 = threading.Thread(target=download_worker)
t2 = threading.Thread(target=file_converter_worker)

t1.start()
t2.start()