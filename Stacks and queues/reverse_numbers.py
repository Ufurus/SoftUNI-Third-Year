numbers = [int(num) for num in input().split()]
for n in range(len(numbers)):
    print(numbers.pop(),end=",")
