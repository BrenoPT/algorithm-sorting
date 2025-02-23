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
    print(f'Time to bubble sort {len(array)} parameters: {round(t2-t1, 4)} seconds')
    return f'Time to bubble sort {len(array)} parameters: {round(t2-t1, 4)} seconds'

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
    print(f'Time to insert sort {len(array)} parameters: {round(t2-t1, 4)} seconds')
    return f'Time to insert sort {len(array)} parameters: {round(t2-t1, 4)} seconds'

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
    print(f'Time to selection sort {len(array)} parameters: {round(t2-t1, 4)} seconds')
    return f'Time to selection sort {len(array)} parameters: {round(t2-t1, 4)} seconds'

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
                                      
            createBubbleSortCalls()
            createInsertSortCalls()
            createSelectionSortCalls()
            
    createCalls()
    
    with open("testResults.json", "w") as json_file:
        json.dump(testResults, json_file, indent=4)
        
testAlgos()
# bubbleSort()
# insertSort()
# selectionSort()

