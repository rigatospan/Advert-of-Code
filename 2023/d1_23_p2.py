file = '2023/d1_23.txt'
dat = open(file).read().splitlines()
num = []
num_letters = {'one': '1' , 'two': '2','three': '3', 'four': '4' ,'five': '5' ,'six': '6' ,'seven': '7' ,'eight': '8' ,'nine': '9'}
num = []
for line in dat: 
    l_numbers = [(c, line.index(c)) for c in line if c.isdigit()]
    l_numbers_r = [(c,len(line)- line[::-1].index(c) -1) for c in line if c.isdigit()]
    l_letters = [(n, line.index(n_l)) for n_l,n in num_letters.items() if n_l in line]
    l_letters_r = [(n, len(line) - line[::-1].index(n_l[::-1]) - len(n_l)) for n_l,n in num_letters.items() if n_l in line]
    l  = sorted(l_letters+l_numbers  + l_letters_r +l_numbers_r, key = lambda x: x[1])
    num.append(int(l[0][0]+l[-1][0]))

print(sum(num))