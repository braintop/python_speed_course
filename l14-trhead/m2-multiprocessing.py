import multiprocessing

# Function to calculate square of a number
def calculate_square(number):
    print(f"Calculating square of {number}")
    return number * number

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Using ProcessPoolExecutor for parallel processing
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(calculate_square, numbers)

    print("Squares:", results)

if __name__ == "__main__":
    main()
