# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
lst = [1,2,3,4,5,6,7,8]
word = "khang"

def sliding_window(items, size):
    if len(lst) < size:
        return items
    for i in range(len(items) - size + 1):
        print(items[i : i + size])

num = sliding_window(lst, 3)
letter = sliding_window(word, 2)
# print(first)
print("")
# print(next(first))

def slide_window(items, size):
    if len(lst) < size:
        return lst
    for i in range(len(items)- size+1):
        yield items[i:i+size]
        
num = slide_window(lst,3)
letter = slide_window(word, 2)
print(next(num))
print(next(num))

print(next(letter))
print(next(letter))