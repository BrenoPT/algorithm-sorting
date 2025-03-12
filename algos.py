import json
import time

def bubbleSort(file):
    try:
        with open(file, "r") as f:
            array = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading {file}: {e}"
    print(f'Bubble sorting {len(array)} parameters...')
    t1 = time.perf_counter()
    
    for i in range(0,len(array) - 1):
        for j in range(0,len(array) - i - 1):
            if(array[j] > array[j+1]):
                temp = array[j] 
                array[j] = array[j+1]
                array[j+1] = temp
    
    t2 = time.perf_counter()
    if all(array[i] <= array[i+1] for i in range(len(array) - 1)):
        print("Bubble Sort Correctly Sorted List.")
    else:
        raise Exception("ERROR: Bubble Sort Incorrectly Sorted List.")
    print(f'Time to bubble sort {len(array)} parameters: {round(t2-t1, 8)} seconds')
    return f'Time to bubble sort {len(array)} parameters: {round(t2-t1, 8)} seconds'

def insertSort(file):
    try:
        with open(file, "r") as f:
            array = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading {file}: {e}"
    print(f'Insert sorting {len(array)} parameters...')
    t1 = time.perf_counter()
    
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while(j >= 0 and array[j] > current):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current 
    
    t2 = time.perf_counter()
    if all(array[i] <= array[i+1] for i in range(len(array) - 1)):
        print("Insert Sort Correctly Sorted List.")
    else:
        raise Exception("ERROR: Insert Sort Incorrectly Sorted List.")
    print(f'Time to insert sort {len(array)} parameters: {round(t2-t1, 8)} seconds')
    return f'Time to insert sort {len(array)} parameters: {round(t2-t1, 8)} seconds'

def selectionSort(file):
    try:
        with open(file, "r") as f:
            array = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading {file}: {e}"
    print(f'Selection sorting {len(array)} parameters...')
    t1 = time.perf_counter()
   
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if(array[j] < array[min]):
                min = j
        if(i != min):
            array[i], array[min] = array[min], array[i]
    
    t2 = time.perf_counter()
    if all(array[i] <= array[i+1] for i in range(len(array) - 1)):
        print("Selection Sort Correctly Sorted List.")
    else:
        raise Exception("ERROR: Selection Sort Incorrectly Sorted List.")
    print(f'Time to selection sort {len(array)} parameters: {round(t2-t1, 8)} seconds')
    return f'Time to selection sort {len(array)} parameters: {round(t2-t1, 8)} seconds'

def mergeSortAlgo(file):
    try:
        with open(file, "r") as f:
            array = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading {file}: {e}"
    print(f'Merge sorting {len(array)} parameters...')
    t1 = time.perf_counter()
    
    def mergeSort(arr):    
        if len(arr) <= 1:
            return arr
           
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
           
        return merge(left, right)
    
    def merge(left, right):
        i = 0
        j = 0
        result = []
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    sorted_array = mergeSort(array)
    t2 = time.perf_counter()
    if all(sorted_array[i] <= sorted_array[i+1] for i in range(len(sorted_array) - 1)):
        print("Merge Sort Correctly Sorted List.")
    else:
        raise Exception("ERROR: Merge Sort Incorrectly Sorted List.")
    print(f'Time to merge sort {len(array)} parameters: {round(t2-t1, 8)} seconds')
    return f'Time to merge sort {len(array)} parameters: {round(t2-t1, 8)} seconds'
    
def quickSortAlgo(file):
    try:
        with open(file, "r") as f:
            array = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error reading {file}: {e}"
    print(f'Quick sorting {len(array)} parameters...')
    t1 = time.perf_counter()
    
    def quickSort(array):
        length = len(array)
        if length <= 1:
            return array
        else:
            pivot = array.pop()
            
        numsBigger = []
        numsSmaller = []
        
        for item in array:
            if item > pivot:
                numsBigger.append(item)
            else:
                numsSmaller.append(item)
        
        return quickSort(numsSmaller) + [pivot] + quickSort(numsBigger)
    
    sorted_array = quickSort(array)
    
    t2 = time.perf_counter()
    if all(sorted_array[i] <= sorted_array[i+1] for i in range(len(sorted_array) - 1)):
        print("Quick Sort Correctly Sorted List.")
    else:
        raise Exception("ERROR: Quick Sort Incorrectly Sorted List.")
    print(f'Time to quick sort {len(array+1)} parameters: {round(t2-t1, 8)} seconds')
    return f'Time to quick sort {len(array+1)} parameters: {round(t2-t1, 8)} seconds'

def testAlgos():
    testResults = []
    try:
        f = open("testResults.json", "x")
    except:
        print("Exception: File exists, overwriting.")
    finally:
        def createCalls():
            def createBubbleSortCalls():
                testResults.append("BUBBLE SORT TIMINGS")
                for i in range(10):
                    amount = 5000 * (i + 1)
                    fileName = f'db{amount}params.json'
                    testResults.append(bubbleSort(fileName))
            
            def createInsertSortCalls():
                testResults.append("INSERT SORT TIMINGS")
                for i in range(10):
                    amount = 5000 * (i + 1)
                    fileName = f'db{amount}params.json'
                    testResults.append(insertSort(fileName))
                    
            def createSelectionSortCalls():
                testResults.append("SELECTION SORT TIMINGS")
                for i in range(10):
                    amount = 5000 * (i + 1)
                    fileName = f'db{amount}params.json'
                    testResults.append(selectionSort(fileName)) 
                                      
            def createMergeSortCalls():
                testResults.append("MERGE SORT TIMINGS")
                for i in range(10):
                    amount = 5000 * (i + 1)
                    fileName = f'db{amount}params.json'
                    testResults.append(mergeSortAlgo(fileName)) 
                    
            def createQuickSortCalls():
                testResults.append("QUICK SORT TIMINGS")
                for i in range(10):
                    amount = 5000 * (i + 1)
                    fileName = f'db{amount}params.json'
                    testResults.append(quickSortAlgo(fileName)) 
            
            createBubbleSortCalls()
            createInsertSortCalls()
            createSelectionSortCalls()
            createMergeSortCalls()
            createQuickSortCalls()
            
    createCalls()
    
    with open("testResults.json", "w") as json_file:
        json.dump(testResults, json_file, indent=4)
        
testAlgos()
# bubbleSort()
# insertSort()
# selectionSort()
# mergeSortAlgo()