lst = [1,2,3,4,5,6,7,8]

def sliding_window(items, size):
    if len(lst) < size:
        return items

first = sliding_window(lst, 3)