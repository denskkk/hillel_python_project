import os
import threading
from multiprocessing import Process
from time import perf_counter

import requests


# CPU-bound task (heavy computation)

def encrypt_file(path: str):
    start_time = perf_counter()
    print(f"Processing image from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    total = perf_counter() - start_time
    print(f"Processed image from {path} in {total:.2f} seconds")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start_time = perf_counter()
    print(
        f"Downloading image from {image_url} in thread ",
        f"{threading.current_thread().name}",
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    total = perf_counter() - start_time
    print(f"Downloaded image from {image_url} in {total:.2f} seconds")


if __name__ == "__main__":
    image_url = "https://picsum.photos/2000/2000"
    start_time = perf_counter()
    # Download image using multiprocessing
    p1 = Process(target=download_image, args=(image_url,))
    p1.start()
    # Encrypt file using multithreading
    p2 = Process(target=encrypt_file, args=("image.jpg",))
    p2.start()
    p1.join()
    p2.join()
    total = perf_counter() - start_time
    print(f"Total time taken: {total:.2f} seconds")
