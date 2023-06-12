import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# urllib takes care of the decoding of the string

counts = dict()

for line in fhand:
    print(line.decode().strip())
    # the lines we get back will be in the form of bytes
    # this is why we need to decode

    for word in line:
        counts[word] = counts.get(word, 0) + 1

print(counts)