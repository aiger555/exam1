example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']
 
def phync(dic, ls):
    for i in ls:
        try:
            plus = 0
            for j in dic[i]:
                try:
                    plus += j
                except TypeError:
                    continue
            print(f'{i} = {plus}')
        except KeyError:
            print(f'The key {i} doesn\'t exist')
phync(example, elements)

