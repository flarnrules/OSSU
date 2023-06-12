import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

# this is essentially the starting part to a web crawler
# it reads a web page
# we now need to learn how to parse this html text