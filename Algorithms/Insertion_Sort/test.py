###  Insertion Sort Algorithm Implementation

"""
Sắp xếp danh sách theo thuật toán Insertion Sort (chèn).
Ý tưởng:
    Insertion Sort hoạt động bằng cách xây dựng dần danh sách đã sắp xếp, phần tử theo phần tử. Mỗi phần tử mới được lấy từ danh sách
    chưa sắp xếp và chèn vào vị trí thích hợp trong danh sách đã sắp xếp, giống như cách ta sắp xếp bài chơi trong tay.
Thuật toán:
    Tại bước k = 1, 2, ..., n đưa phần tử thứ k trong mảng đã cho vào đúng vị trí trong dãy gồm k phần tử đầu tiên.
    Kết quả là sau bước thứ k, sẽ có k phần tử đầu tiên được sắp xếp theo thứ tự.
Tham số:
    arr (list): Danh sách các phần tử có thể so sánh với nhau.
Trả về:
    list: Danh sách arr đã được sắp xếp (cùng đối tượng đầu vào, được sửa tại chỗ).
Tính chất:
    - Ổn định: Có (giữ nguyên thứ tự tương đối của các phần tử bằng nhau).
    - Độ phức tạp thuật toán: O(n^2) trung bình và tồi tệ; O(n) trong trường hợp tốt khi danh sách đã gần như được sắp xếp.
    - Độ phức tạp bộ nhớ: O(1) (in-place).
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
