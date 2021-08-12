# 1
# 1.1 - str
# 1.2 - bool
# 1.3 - dict
# 1.4 - set
# 1.5 - None
# 1.6 - None
# 1.7 - первые 4 значений -str, остальные - int
# 1.8 - str
# 1.9 - list
# 1.10 - str

# 2
def bank(deposit, last_sum, percent):
    month = 0
    first_sum = deposit
    while  first_sum < last_sum:
        first_sum = percent/100/12*first_sum+first_sum
        month += 1
    return month

print(bank(1000, 3500, 30))

# 3.1
# ls = ['Element', 'start', 'finish']
# def lst(*args):
#     ls.insert(2, args)
#     return ls
# print(lst(*['hello', 5, 'John', ]))

# 3.2
# def d(*args):
#     dict_keys = list(args)
#     dict_values = [1, 2, 3]
#     dict_zipped = dict(zip(dict_keys, dict_values))
#     return dict_zipped
        
    
# print(d('x', 5, 'John')) 

# 3.3
# def func(args):
#    args = list(args)
#    a = [x for x in args if x % 2 == 0]
#    print(a)
#    lst = []
#    for i in args:
#         i = i**2
#         lst.append(i)
#    print(lst)
# print(func((1,2,3,4,5)))

