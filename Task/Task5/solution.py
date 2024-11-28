
class Item:
    def __init__(self,id=0):
        self.id = id
        self.time = 0
        self.last_idx = 0

    def update_time_by_id(self,id,last_idx):
        if self.id == id:
            self.time += 1
            self.last_idx = last_idx

def solution(T):
    items = []
    for i in range(len(T)):
        items.append(Item(i))

    sum_T = sum(T)
    order = []
    idx = 0

    while len(order) < sum_T:
        if idx == len(items):
            idx = 0
        if items[idx].time < T[idx]:
            items[idx].update_time_by_id(idx,len(order))
            order.append(items[idx])
        idx += 1

    total_time = [item.last_idx + 1 for item in items]

    return sum(total_time) % 10**9
