from time import process_time


arr = [
    "nem",
    "nemo",
]


def findNemo(arr):
    t0 = process_time()
    
    for i in range(len(arr)): # o(n)
        if arr[i] == "nemo":
            t1 = process_time()
            print("Call to find Nemo took " + str(t1 - t0) + " seconds")
            return i
    t1 = process_time()
    print("Call to find Nemo took " + str(t1 - t0) + " seconds")



print(findNemo(arr))
# o(n) - linear time complexity | space complexity o(1)