def recursion(num):
    if num == 0:
        print(num, end=" --> ")
    else:
        print(num, end=" --> ")
        recursion(num - 1)

print(recursion(5))