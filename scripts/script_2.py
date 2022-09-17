from random import randint

path_to = 'dict.txt'
n = 10000

with open(path_to, 'w') as f:
    pass

with open(path_to, 'a') as f:
    for i in range(n):
        num = str(randint(1000, 9999)) + '  ' + str(randint(1000, 9999)) + '  ' + str(randint(1000, 9999)) + '  ' + str(randint(1000, 9999))
        f.write(num + '\n')