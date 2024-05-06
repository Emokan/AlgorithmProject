import time
import random
import matplotlib.pyplot as plt

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
              arr[k] = L[i]
              i += 1
            else:
              arr[k] = R[j]
              j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def measure_time(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    return time.time() - start_time

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def plot_runtime_comparison(max_size=1000, step=10):
    insertion_times = []
    merge_times = []
    sizes = list(range(1, max_size + 1, step))
    merge_sort_outperforms = False  # Flag to check if Merge Sort has outperformed Insertion Sort

    for size in sizes:
        # Generate a random array of size `size`
        # If the array is already sorted, generate a new array so that we can avoid the noise
        while size > 1:
            arr = [random.randint(1, 1000) for _ in range(size)]
            
            if not is_sorted(arr):
                break
        if size <= 1:
            arr = [random.randint(1, 1000) for _ in range(size)]
        insertion_time = measure_time(insertion_sort, arr.copy())
        merge_time = measure_time(merge_sort, arr.copy())
        
        # If the time is less than 2 microseconds, set it to 0
        # This is to avoid the noise in the data due to the time.time() function
        if insertion_time < 0.000002:
            insertion_time = 0
        if merge_time < 0.000002:
            merge_time = 0
        
        insertion_times.append(insertion_time)
        merge_times.append(merge_time)
        # If Merge Sort outperforms Insertion Sort, plot a red dot and label it
        if (not merge_sort_outperforms) and (merge_time < insertion_time):
            merge_sort_outperforms = True
            plt.scatter(size, merge_time, color='red', marker='o', label=f'Merge Sort Outperforms at Size {size}\nMerge Time: {merge_time:.6f}s\nInsertion Time: {insertion_time:.6f}s')
        

    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Insertion Sort vs. Merge Sort Runtime Comparison')
    plt.show()

# Run the plot
plot_runtime_comparison()