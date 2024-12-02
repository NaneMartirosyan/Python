import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def process_and_write_back(file_name="random_numbers.txt"):
    with open(file_name, "r") as f:
        lines = f.readlines()  

    filtered_lines = [
        " ".join(str(num) for num in map(int, line.split()) if num > 40)
        for line in lines
    ]
    
    with open(file_name, "w") as f:
        f.write("\n".join(filtered_lines) + "\n")  
    print(f"Filtered data written back to '{file_name}'.")

def read_file_generator(file_name="random_numbers.txt"):
    with open(file_name, "r") as f:
        for line in f:
            yield [int(num) for num in line.split()]  

@measure_time
def process_with_generator(file_name="random_numbers.txt"):
    generator = read_file_generator(file_name)
    for line in generator:
        print(f"Processed Line: {line}")  

process_and_write_back()  
process_with_generator()  

