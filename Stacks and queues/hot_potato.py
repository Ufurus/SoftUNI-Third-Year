from collections import deque
chosen_kids = deque(input().split())
number_of_tosses = int(input())

while len(chosen_kids) != 1:

    chosen_kids.rotate(-number_of_tosses + 1)
    print(f"Removed {chosen_kids.popleft()}")

print(f"Last is {chosen_kids.pop()}")