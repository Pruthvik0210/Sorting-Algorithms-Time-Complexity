import time
from project import bubble_sort, insertion_sort, selection_sort, heap_sort, merge_sort, quick_sort, quick_sort_three_medians


def bubble(data):
    start = time.time()
    bubble_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken


def insertion(data):
    start = time.time()
    insertion_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken


def selection(data):
    start = time.time()
    selection_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken


def heap(data):
    start = time.time()
    heap_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken


def merge(data):
    start = time.time()
    merge_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken


def quick(data, drawData):
    start = time.time()
    sorted = quick_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    # sorted elements geneated with Green color
    drawData(sorted, ['Green' for x in range(len(data))])
    return timeTaken


def quicks(data):
    start = time.time()
    sorted = quick_sort(data)
    end = time.time()
    timeTaken = str(end - start)
    return timeTaken,sorted


def quick_tm(data):
    start = time.time()
    quick_sort_three_medians(data, 0, len(data) - 1)
    end = time.time()
    timeTaken = str(end - start)
    # drawData(data, ['Green' for x in range(len(data))])
    return timeTaken




