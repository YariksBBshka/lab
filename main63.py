def sameel(arr1, arr2):
    stack = []
    for i in range(0, len(arr2)):
        for j in range(0, len(arr1)):
            if arr2[i] == arr1[j]:
                stack.append(arr2[i])
    if stack == []:
        return "No matches!"
    return " ".join(stack)
mas1 = input().split(" ")
mas2 = input().split(" ")
print(sameel(mas1, mas2).strip())
