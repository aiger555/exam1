from random import randint

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']
nano = names[randint(0, len(names)) - 1]
with open(nano, 'w') as new:
    pass

def func(f_names):
    for i in f_names:
        try:
            with open(i, 'r+') as f:
                f.write('Aigerim')
        except FileNotFoundError:
            print(f'The {i} does not exist')

func(names)