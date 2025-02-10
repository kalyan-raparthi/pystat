def prob(arr, index):
    recur = 0
    for i in arr:
        if (arr[index] == i):
            recur += 1
    return ((recur / len(arr)) * 100)
  

# usage of probability funtion
# arr = [1, 2, 3, 4, 5, 6]
# print(prob(arr, arr.index(2)))
