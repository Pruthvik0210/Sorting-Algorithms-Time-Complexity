"""
Pruthvik Kakadiya
Design & Analysis of algorithms project
Id : 1001861545
Project 1 : Sorting Algorithms
"""

import random  # import random to get random numbers for algorithm
import time    # import time to calculate time complexity of any algorithm
import matplotlib.pyplot as plt   # install and import matplotlib.pyplot to see in a graph form


#ds_s = []
# get different sizes of datasets
def get_dataset_sizes():
    ds_s = []
    n = int(input("Enter no of how many different Dataset sizes you want to be compared: "))
    print("Enter different Dataset sizes (followed by enter): ")
    for i in range(0, n):
        sizes = int(input())
        ds_s.append(sizes)
    print("Dataset sizes are: ", ds_s)
    return ds_s


'''
count = int(input("Enter no of how many different Dataset sizes you want to be compared: "))
for i in range(1,count):
    ds_s.append(i)
'''


# to get random integer dataset of size n
def dataset_of_size(n):
    x = []
    for i in range(n):
        num_temp = random.randint(0, n)
        x.append(num_temp)
    # print(x)  # to print dataset of size n
    return x


# to get different datasets of different sizes
def datasets(dataset_sizes):
    dataset = {}  # Dictionary of datasets having different sizes (format: 'Dataset_of_size:n': []
    for i in range(0, len(dataset_sizes)):
        dataset['Dataset_of_size : ' + str(dataset_sizes[i])] = dataset_of_size(dataset_sizes[i])
    # print(dataset) # to print all datasets
    return dataset


# to run merge sort for different datasets having different sizes
def run_merge_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)     #to print dataset before sorting
    i = 0
    t_m = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = merge_sort(value)
        # merge_sort(value)
        end = time.time()
        t_m.append(end - start)
        print(len(ds_s), "Data_size Sorted by MergeSort  ", end - start)
        i += 1
    # print('merge', sorted_dataset)     #to print dataset after sorting
    return t_m


# to run heap sort for different datasets having different sizes
def run_heap_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)     #to print dataset before sorting
    i = 0
    t_h = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = heap_sort(value)
        # heap_sort(value)
        end = time.time()
        t_h.append(end - start)
        print(len(value), "Data_size Sorted by HeapSort  ", end - start)
        i += 1
    # print('heap', sorted_dataset)     #to print dataset before sorting
    return t_h


def run_quick_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)     #to print dataset before sorting
    i = 0
    t_q = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = quick_sort(value)
        # quick_sort(value)
        end = time.time()
        t_q.append(end - start)
        print(len(value), "Data_size Sorted by QuickSort  ", end - start)
        i += 1
    # print('quick', sorted_dataset)     #to print dataset before sorting
    return t_q


def run_quick_sort_three_medians():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)     #to print dataset before sorting
    i = 0
    t_q_three = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = quick_sort_three_medians(value, 0, len(value)-1)
        # quick_sort_three_medians(value, 0, len(value)
        end = time.time()
        t_q_three.append(end - start)
        print(len(value), "Data_size Sorted by QuickSort with three medians  ", end - start)
        i += 1
    # print('quick_3_medians', sorted_dataset)
    return t_q_three


# to run insertion sort for different datasets having different sizes
def run_insertion_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)      #to print dataset before sorting
    i = 0
    t_i = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = insertion_sort(value)
        # insertion_sort(value)
        end = time.time()
        t_i.append(end - start)
        print(len(value), "Data_size Sorted by InsertionSort  ", end - start)
        i += 1
    # print('insertion', sorted_dataset)     #to print dataset before sorting
    return t_i


# to run selection sort for different datasets having different sizes
def run_selection_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)    #to print dataset before sorting
    i = 0
    t_s = []
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = selection_sort(value)
        # selection_sort(value)
        end = time.time()
        t_s.append(end - start)
        print(len(value), "Data_size Sorted by SelectionSort  ", end - start)
        i += 1
    # print('selection', sorted_dataset)    #to print dataset before sorting
    return t_s


# to run bubble sort for different datasets having different sizes
def run_bubble_sort():
    dataset = datasets(ds_s)
    sorted_dataset = {}  # Dictionary of sorted datasets having different sizes (format: 'Sorted dataset:n': []
    # print('before', dataset)     #to print dataset before sorting
    i = 0
    t_b = []  # array to store execution time taken by bubble sort
    for value in dataset.values():
        start = time.time()
        sorted_dataset['Sorted_dataset : ' + str(ds_s[i])] = bubble_sort(value)
        # bubble_sort(value)
        end = time.time()
        t_b.append(end - start)
        print(len(value), "Data_size Sorted by BubbleSort  ", end - start)
        i += 1
    # print('bubble', sorted_dataset)     #to print dataset before sorting
    return t_b


# merge sort
def merge_sort(x):  # x is array of integers(data set)
    if len(x) > 1:
        mid = len(x) // 2
        l = x[:mid]
        r = x[mid:]
        merge_sort(l)
        merge_sort(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                x[k] = l[i]
                i += 1
            else:
                x[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            x[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            x[k] = r[j]
            j += 1
            k += 1
    return x


def heapify(x, n, i):
    maximum = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and x[i] < x[l]:
        maximum = l
    if r < n and x[maximum] < x[r]:
        maximum = r

    if maximum != i:
        swap = x[i]
        x[i] = x[maximum]
        x[maximum] = swap
        heapify(x, n, maximum)


# heap sort
def heap_sort(x):
    n = len(x)
    for i in range(n // 2, -1, -1):
        heapify(x, n, i)
    for i in range(n - 1, 0, -1):
        swap = x[0]
        x[0] = x[i]
        x[i] = swap
        heapify(x, i, 0)
    return x


# insertion sort
def insertion_sort(x):  # x is array of integers(dataset)
    l = 0
    r = len(x) - 1
    for i in range(l + 1, r + 1):
        k = x[i]
        j = i - 1
        while j >= 0 and k < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = k
    return x


def quick_sort(x):
    n = len(x)
    if n < 2:
        return x
    current = 0
    for i in range(1, n):
        if x[i] <= x[0]:
            current += 1
            x[i], x[current] = x[current], x[i]
    temp = x[0]
    x[0] = x[current]
    x[current] = temp
    left = quick_sort(x[0: current])  # sort left side of pivot
    right = quick_sort(x[current + 1: n])  # sort right side of pivot
    x = left + [x[current]] + right  # merging everything
    return x


def partition3(x, l, r):
    lt = l
    i = l
    gt = r
    pivot = x[l]
    while i <= gt:
        if x[i] < pivot:
            x[lt], x[i] = x[i], x[lt]
            lt += 1
            i += 1
        elif x[i] > pivot:
            x[i], x[gt] = x[gt], x[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def quick_sort_three_medians(x, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    x[k], x[l] = x[l], x[k]

    lt, gt = partition3(x, l, r)
    quick_sort_three_medians(x, l, lt - 1)
    quick_sort_three_medians(x, gt + 1, r)
    return x

# selection sort
def selection_sort(x):
    for i in range(len(x)):
        minimum = i
        for j in range(i + 1, len(x)):
            if x[minimum] > x[j]:
                minimum = j
        swap = x[i]
        x[i] = x[minimum]
        x[minimum] = swap
    return x


# bubble sort
def bubble_sort(x):
    l = x
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if l[i] > l[j]:
                swap = l[i]
                l[i] = l[j]
                l[j] = swap
    return l
    # print(l)  # to print sorted array


def count_time():
    t_b_s = run_bubble_sort()      # array of time complexities for bubble sort in seconds
    t_s_s = run_selection_sort()   # array of time complexities for selection sort in seconds
    t_i_s = run_insertion_sort()   # array of time complexities for insertion sort in seconds
    t_h_s = run_heap_sort()        # array of time complexities for heap sort in seconds
    t_m_s = run_merge_sort()       # array of time complexities for merge sort in seconds
    t_q_s = run_quick_sort()       # array of time complexities for quick sort in seconds
    t_q_t_s = run_quick_sort_three_medians()

    print("Dataset sizes are: ", ds_s)
    print("Bubble sort    : ", t_b_s)
    print("Selection sort : ", t_s_s)
    print("Insertion sort : ", t_i_s)
    print("Heap sort      : ", t_h_s)
    print("Merge sort     : ", t_m_s)
    print("Quick sort     : ", t_q_s)
    print("Quick 3 medians: ", t_q_t_s)

    plt.plot(ds_s, t_b_s, label="Bubble sort", color="k")
    plt.plot(ds_s, t_s_s, label="Selection sort", color="r")
    plt.plot(ds_s, t_i_s, label="Insertion sort", color="b")
    plt.plot(ds_s, t_h_s, label="Heap sort", color="g")
    plt.plot(ds_s, t_m_s, label="Merge sort", color="y")
    plt.plot(ds_s, t_q_s, label="Quick sort", color="m")
    plt.plot(ds_s, t_q_t_s, label="Quick 3 medians", color="c")
    plt.xlabel("Size of Dataset")
    plt.ylabel("Time in Seconds")
    plt.legend()
    plt.show()

def get_user_data():
    print("")
    user_data = input('Enter the list of numbers separated by spaces: ').split()
    u_d = [int(x) for x in user_data]
    # print(user_data)
    return u_d


def main():
    while True:
        print("")
        print("Choose from following")
        print("")
        print("1: Compare time complexities of all algorithms using user given different Dataset sizes ")
        print("2: Run sorting algorithm and provide Sorted Dataset using User Given Dataset ")
        print("3: GUI to visualize sort")
        print("4: GUI to compare time complexity of algorithms")
        print("5: exit")
        ch1 = int(input())
        if ch1 == 1:
            global ds_s
            ds_s = get_dataset_sizes()
            '''
            # implemented this to run time complexities from dataset sizes 0 to n 
            count = int(input("Enter no of how many different Dataset sizes you want to be compared: "))
            for i in range(1,count):
                ds_s.append(i)
            '''
            count_time()
        if ch1 == 2:
            while True:
                print("Choose from following sorting algorithm")
                print("1:Bubble sort")
                print("2:Selection sort")
                print("3:Insertion sort")
                print("4:Heap sort")
                print("5:Merge sort")
                print("6:Quick sort")
                print("7:Quick 3 medians sort")
                print("8: exit")
                ch2 = int(input())
                if ch2 == 1:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = bubble_sort(u_d)
                    print(s_d)
                if ch2 == 2:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = selection_sort(u_d)
                    print(s_d)
                if ch2 == 3:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = insertion_sort(u_d)
                    print(s_d)
                if ch2 == 4:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = heap_sort(u_d)
                    print(s_d)
                if ch2 == 5:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = merge_sort(u_d)
                    print(s_d)
                if ch2 == 6:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = quick_sort(u_d)
                    print(s_d)
                if ch2 == 7:
                    u_d = get_user_data()
                    print(u_d)
                    s_d = quick_sort_three_medians(u_d, 0, len(u_d) - 1)
                    print(s_d)
                if ch2 == 8:
                    return False
        if ch1 == 3:
            import tk
        if ch1 == 4:
            import tk_compare
        if ch1 == 5:
            return False


if __name__ == "__main__":
    main()


"""
References :
Stack Overflow
Geeks for Geeks
W3 school
Real python
"""
