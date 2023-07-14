import re
import sqlite3
import urllib.request

# Connect to the database
conn = sqlite3.connect('count.sqlite')
cur = conn.cursor()

# Drop the table if it already exists and create a new one
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Regular expression to match 'From ' followed by an email address
email_regex = r'^From\s+([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})'

url = 'http://www.py4e.com/code3/mbox.txt'
try:
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    response = urllib.request.urlopen(req)
    for line in response:
        line = line.decode().strip()
        match = re.search(email_regex, line)
        if match:
            email = match.group(1)  # Extract the email address
            org = email.split('@')[1]  # Get the domain part
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                            (org,))

except urllib.error.URLError as e:
    print(f"Could not retrieve {url}: {e.reason}")
    exit()

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
