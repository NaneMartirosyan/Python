import os
import random
import string
import time
from collections import Counter
from threading import Thread, Lock
from multiprocessing import Process, Manager


def generate_large_text_file(filename, num_words):
    with open(filename, 'w') as f:
        for _ in range(num_words):
            word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
            sentence = ' '.join([word for _ in range(random.randint(5, 15))])
            f.write(sentence + '.\n')


def count_words_sequential(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return Counter(words)


def count_words_multithreading(filename, num_threads=4):
    def worker(chunk, word_count, lock):
        local_count = Counter(chunk.split())
        with lock:
            word_count.update(local_count)

    with open(filename, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    word_count = Counter()
    lock = Lock()
    threads = []

    for chunk in chunks:
        thread = Thread(target=worker, args=(' '.join(chunk), word_count, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_count


def count_words_multiprocessing(filename, num_processes=4):
    def worker(chunk, return_dict):
        local_count = Counter(chunk.split())
        return_dict.append(local_count)

    with open(filename, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_processes
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    manager = Manager()
    return_dict = manager.list()
    processes = []

    for chunk in chunks:
        process = Process(target=worker, args=(' '.join(chunk), return_dict))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_count = Counter()
    for local_count in return_dict:
        total_count.update(local_count)

    return total_count


def compare_methods(filename):
    print("Comparing methods...")

    start = time.time()
    seq_result = count_words_sequential(filename)
    seq_time = time.time() - start
    print(f"Sequential: {seq_time:.4f} seconds")

    start = time.time()
    thread_result = count_words_multithreading(filename)
    thread_time = time.time() - start
    print(f"Multithreading: {thread_time:.4f} seconds")

    start = time.time()
    process_result = count_words_multiprocessing(filename)
    process_time = time.time() - start
    print(f"Multiprocessing: {process_time:.4f} seconds")


    print(f"Speedup with multithreading: {seq_time / thread_time:.2f}x")
    print(f"Speedup with multiprocessing: {seq_time / process_time:.2f}x")


if __name__ == "__main__":
    FILENAME = 'large_text_file.txt'
    NUM_WORDS = 10**6 
    if not os.path.exists(FILENAME):
        print("Generating large text file...")
        generate_large_text_file(FILENAME, NUM_WORDS)

    compare_methods(FILENAME)
