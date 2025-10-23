###  Selection Sort Algorithm Implementation

"""
Sắp xếp danh sách theo thuật toán Selection Sort (chèn).
Ý tưởng:
    Ý tưởng của Selection sort là tìm từng phần tử cho mỗi vị trí của mảng hoán vị A' cần tìm.
Thuật toán:
    Tìm phần tử nhỏ nhất đưa vào vị trí 1
    Tìm phần tử nhỏ tiếp theo đưa vào vị trí 2
    Tìm phần tử nhỏ tiếp theo đưa vào vị trí 3
    ...
    Lặp lại cho đến khi mảng được sắp xếp hoàn toàn.
Tham số:
    arr (list): Danh sách các phần tử có thể so sánh với nhau.
Trả về:
    list: Danh sách arr đã được sắp xếp (cùng đối tượng đầu vào, được sửa tại chỗ).
Tính chất:
    - Không ổn định: Có thể thay đổi thứ tự tương đối của các phần tử bằng nhau.
    - Độ phức tạp thuật toán: O(n^2) trong mọi trường hợp (tốt, trung bình, tồi tệ).
    - Độ phức tạp bộ nhớ: O(1) (in-place).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
