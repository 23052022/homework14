a = int(input("Enter number:"))
def square(x):
    if x < 2:
        return x
    r = 0
    left = 0
    right = x
    while left <= right:
        middle = (left + right) // 2
        if middle * middle == x:
            return middle
        elif middle * middle < x:
            left = middle + 1
            r = middle
        else:
            right = middle - 1
    return r
print(square(a))