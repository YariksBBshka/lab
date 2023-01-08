def rev(arr):
    stack = []
    for i in range(len(arr)):
        stack.append(arr.pop())
    return (", ".join((stack)).strip())
arr = input().split(", ")
print(rev(arr))

def rev2(arr):
    stack = []
    n = 0
    for i in range(0, len(arr)):
        n += 1
        stack.append(arr[len(arr) - n])
    return stack
arr = input().split(", ")
print(", ".join(rev2(arr)))
