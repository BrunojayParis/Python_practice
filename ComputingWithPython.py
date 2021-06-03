#computing With Python from the free code camp 

#Word count in a file.

name = input('Enter a file name: ')
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print (counts)
print ('counting words... ')

bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

