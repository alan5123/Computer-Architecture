# Add up and print the sum of the all of the minimum elements of each inner array:
random = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
sum = 0
for arr in random:
  min = arr[0]
  for i in range(len(arr)):
    if arr[i] < min:
      min = arr[i]
  sum += min
print(sum)
