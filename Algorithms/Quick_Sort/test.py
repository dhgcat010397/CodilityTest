###  Quick Sort Algorithm Implementation

"""
Sắp xếp danh sách theo thuật toán Quick Sort.
Ý tưởng:
    Quick Sort là thuật toán sắp xếp theo phương pháp chia để trị (divide and conquer). Ý tưởng chính là chọn một phần tử làm 
    chốt (pivot), sau đó phân vùng mảng sao cho các phần tử nhỏ hơn chốt nằm bên trái và các phần tử lớn hơn chốt nằm bên phải. 
    Quá trình này được lặp lại đệ quy cho các phân vùng con cho đến khi mảng được sắp xếp hoàn chỉnh.
Thuật toán:
    1. Chọn một phần tử làm chốt (pivot).
    2. Phân vùng mảng sao cho các phần tử nhỏ hơn chốt nằm bên trái và các phần tử lớn hơn chốt nằm bên phải.
    3. Áp dụng đệ quy Quick Sort cho các phân vùng con bên trái và bên phải của chốt.
Tham số:
    arr (list): Danh sách các phần tử có thể so sánh với nhau.    
Trả về:
    list: Danh sách arr đã được sắp xếp (mảng mới).
Tính chất:
    - Không ổn định: Có thể thay đổi thứ tự tương đối của các phần tử bằng nhau.
    - Độ phức tạp thuật toán: O(n log n) trung bình và tốt; O(n^2) tồi tệ (khi mảng đã được sắp xếp hoặc gần như sắp xếp).
    - Độ phức tạp bộ nhớ: O(log n) do sử dụng ngăn xếp đệ quy.    
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)
