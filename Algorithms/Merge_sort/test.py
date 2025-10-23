###  Merge Sort Algorithm Implementation

"""
Sắp xếp danh sách theo thuật toán Merge Sort (trộn).
Ý tưởng:
    Merge Sort là thuật toán sắp xếp theo phương pháp chia để trị (divide and conquer). Ý tưởng chính là chia mảng thành các 
    phần nhỏ hơn cho đến khi mỗi phần chỉ còn một phần tử, sau đó trộn các phần đã sắp xếp lại với nhau để tạo thành mảng đã 
    được sắp xếp hoàn chỉnh.
Thuật toán:
    1. Chia: Chia mảng ban đầu thành hai nửa cho đến khi mỗi mảng con chỉ còn một phần tử.
    2. Trộn: Trộn các mảng con đã sắp xếp lại với nhau để tạo thành mảng lớn hơn đã được sắp xếp.
Tham số:
    arr (list): Danh sách các phần tử có thể so sánh với nhau.
Trả về:
    list: Danh sách arr đã được sắp xếp (cùng đối tượng đầu vào, được sửa tại chỗ).
Tính chất:
    - Ổn định: Có (giữ nguyên thứ tự tương đối của các phần tử bằng nhau).
    - Độ phức tạp thuật toán: O(n log n) trong mọi trường hợp (tốt, trung bình, tồi tệ).
    - Độ phức tạp bộ nhớ: O(n) (không in-place).
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]   # left half: arr[0..mid-1]
        R = arr[mid:]   # right half: arr[mid..end]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # if len(L) > len(R)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # if len(R) > len(L)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
