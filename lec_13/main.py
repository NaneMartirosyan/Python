import random
import string
import time
import threading
from multiprocessing import Pool, Manager

def generate_text_file(filename, num_sentences=10000):
    """Generates a large text file with random words and sentences."""
    with open(filename, 'w', encoding='utf-8') as file:
        for _ in range(num_sentences):
            num_words = random.randint(5, 15)
            sentence = ' '.join(
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(num_words)
            )
            file.write(sentence + '.\n')

def count_words_sequential(filename):
    """Counts words in the file sequentially."""
    word_count = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

def process_chunk_threading(chunk, thread_shared_counts):
    """Processes a file chunk for multithreading."""
    local_count = {}
    for line in chunk:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in local_count:
                local_count[word] += 1
            else:
                local_count[word] = 1

    with threading.Lock():
        for word, count in local_count.items():
            if word in thread_shared_counts:
                thread_shared_counts[word] += count
            else:
                thread_shared_counts[word] = count

def count_words_multithreading(filename, num_threads=4):
    """Counts words in the file using multithreading."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    thread_shared_counts = {}

    for i in range(num_threads):
        chunk = lines[i * chunk_size : (i + 1) * chunk_size]
        thread = threading.Thread(target=process_chunk_threading, args=(chunk, thread_shared_counts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return thread_shared_counts

def process_chunk_multiprocessing(chunk):
    """Processes a file chunk for multiprocessing."""
    local_count = {}
    for line in chunk:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in local_count:
                local_count[word] += 1
            else:
                local_count[word] = 1
    return local_count

def count_words_multiprocessing(filename, num_processes=4):
    """Counts words in the file using multiprocessing."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    chunks = [lines[i * chunk_size : (i + 1) * chunk_size] for i in range(num_processes)]

    with Manager() as manager:
        process_shared_counts = manager.dict()
        with Pool(processes=num_processes) as pool:
            results = pool.map(process_chunk_multiprocessing, chunks)

        for result in results:
            for word, count in result.items():
                if word in process_shared_counts:
                    process_shared_counts[word] += count
                else:
                    process_shared_counts[word] = count

        return dict(process_shared_counts)

def compare_execution_time(filename):
    """Compares execution times of sequential, multithreading, and multiprocessing word counting."""
    print("Comparing execution times...")

    # Sequential
    start = time.time()
    sequential_counts = count_words_sequential(filename)
    sequential_duration = time.time() - start
    print(f"Sequential method took {sequential_duration:.4f} seconds")

    # Multithreading
    start = time.time()
    thread_counts = count_words_multithreading(filename, num_threads=4)
    thread_duration = time.time() - start
    print(f"Multithreading method took {thread_duration:.4f} seconds")

    # Multiprocessing
    start = time.time()
    process_counts = count_words_multiprocessing(filename, num_processes=4)
    process_duration = time.time() - start
    print(f"Multiprocessing method took {process_duration:.4f} seconds")

    # Validate results
    assert sequential_counts == thread_counts == process_counts, "The results do not match!"

    # Speedup
    threading_speedup = sequential_duration / thread_duration
    multiprocessing_speedup = sequential_duration / process_duration

    print(f"Speedup (Multithreading): {threading_speedup:.2f}")
    print(f"Speedup (Multiprocessing): {multiprocessing_speedup:.2f}")

if __name__ == "__main__":
    filename = 'large_text_file.txt'
    generate_text_file(filename, num_sentences=10000)
    compare_execution_time(filename)
