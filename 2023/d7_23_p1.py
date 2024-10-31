cards = [line.split() for line in open('d7_23.txt').read().splitlines()]
chrs = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4','3', '2']
value = list('abcdefghiklmn')
d = {chrs[i]:value[i] for i in range(len(chrs))}
d_rev = {value[i]:chrs[i] for i in range(len(chrs))}

five , four, fullhous, three, twopairs, onepair, highcard = [],[],[],[],[],[],[]
categories = {'55555':five , '14444':four, '22333':fullhous, '11333':three, 
              '12222': twopairs, '11122': onepair, '11111':highcard}

for card, value in cards:
    counting = ''.join([str(s) for s in sorted([card.count(c) for c in card])])
    for cat in categories.keys():
        if counting == cat:
            categories[cat].append((card, value))

sort_cat = []
for c in categories.values():
    c_valued = [(''.join([d[char] for char in card]),value) for card,value in c]
    c = sorted(c_valued, reverse=True)
    c = [(''.join([d_rev[char] for char in card]), value) for card, value in c]
    sort_cat.append(c)

rank = 1
winnings = 0
for category in reversed(sort_cat):
    for card, value in category:
        winnings += int(value)*rank
        rank+=1
        
print(winnings)