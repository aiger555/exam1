# 1
# 1.1 - str
# 1.2 - str
# 1.3 - int
# 1.4 - set
# 1.5 - int
# 1.6 - list
# 1.7 - первые 4 значений -str, остальные - int
# 1.8 - str
# 1.9 - list
# 1.10 - str

# 2
# sum_of_deposit = int(input('Enter deposit amount: '))
# month = input('Enter month: ')
# yearP = int(input('Enter annual percentage: '))

# def sm(sum_of_deposit, month, yearP):
#     annual = yearP / 100
#     total = annual/ month * sum_of_deposit + sum_of_deposit
#     next = annual/ month * total + total
#     months = total + next
#     return months
# print(sm(yearP, sum_of_deposit, yearP))

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

