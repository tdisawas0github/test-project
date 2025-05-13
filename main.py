def calculator(a, b):
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    print(f"Quotient: {a / b}")

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:", a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is: {fact}")

def prime(n):
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                is_prime = False
                break
    print(f"{n} is {'a' if is_prime else 'not a'} prime number.")

def palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    print(f"{original} is {'a' if original == reversed_num else 'not a'} palindrome.")

def armstrong(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    print(f"{original} is {'an' if original == total else 'not an'} Armstrong number.")

def reverse(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    print(f"Reversed number: {reversed_num}")

def swap(a, b):
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array:", " ".join(map(str, arr)))

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            print(f"Element found at index: {mid}")
            return
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    print("Element not found.")

def linear_search(arr, key):
    for i, val in enumerate(arr):
        if val == key:
            print(f"Element found at index: {i}")
            return
    print("Element not found.")

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]
    
    i = j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", " ".join(map(str, arr)))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Sorted array:", " ".join(map(str, arr)))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array:", " ".join(map(str, arr)))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def binary_tree():
    # Binary tree implementation can be added here
    pass

if __name__ == "__main__":
    pass