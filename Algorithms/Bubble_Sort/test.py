###  Bubble Sort Algorithm Implementation

"""
Sắp xếp danh sách theo thuật toán Bubble Sort (nổi bọt).
Ý tưởng:
    Bubble Sort, như cái tên của nó, là thuật toán đẩy phần tử lớn nhất xuống cuối dãy, đồng thời những phần tử có giá trị nhỏ hơn sẽ 
    dịch chuyển dần về đầu dãy. Tựa như sự nổi bọt vậy, những phần tử nhẹ hơn sẽ nổi lên trên và ngược lại, những phần tử lớn hơn sẽ 
    chìm xuống dưới.
Thuật toán:
    Duyệt mảng từ phần tử đầu tiên. Ta sẽ so sánh mỗi phần tử với phần tử liền trước nó, nếu chúng đứng sai vị trí, ta sẽ đổi chỗ chúng 
    cho nhau. Quá trình này sẽ được dừng nếu gặp lần duyệt từ đầu dãy đến cuối dãy mà không phải thực hiện đổi chỗ bất kì 2 phần từ nào 
    (tức là tất cả các phần tử đã được sắp xếp đúng vị trí).
Tham số:
    arr (list): Danh sách các phần tử có thể so sánh với nhau.
Trả về:
    list: Danh sách arr đã được sắp xếp (cùng đối tượng đầu vào, được sửa tại chỗ).
Tính chất:
    - Ổn định: Có (giữ nguyên thứ tự tương đối của các phần tử bằng nhau).
    - Độ phức tạp thuật toán: O(n^2) trung bình và tồi tệ; trong triển khai hiện tại cũng O(n^2) ở trường hợp tốt vì không có tối ưu dừng 
    sớm.
    - Độ phức tạp bộ nhớ: O(1) (in-place).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
