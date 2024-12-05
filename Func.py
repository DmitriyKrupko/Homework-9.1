def gen_list(x, y):
    lst = []
    while(x < y + 1):
        lst.append(x)
        x += 1
    return lst
def modify_list(lst):
    res = [i for i in lst if i%2 != 0]
    return res
