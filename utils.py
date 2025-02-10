# probability funtion

def probability(arr, index):
  recur = 0
  for i in arr:
    if (arr[index] == i):
      recur += 1
  return (recur / len(arr))

