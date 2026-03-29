import urllib.request
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTeZOZkkus3PIv-QuhZTT83J9_C3WYGC7rhzg_DyiAaBkn0nE0Ec7nqU-AGkkHz8a06aUK9AR8pliT4/pub?gid=0&single=true&output=csv'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as response:
    data = response.read().decode('utf-8')

lines = data.strip().split('\n')
print(f"Total rows: {len(lines)}")
for i, line in enumerate(lines[:5]):
    # Print each cell separately
    cells = line.split(',')
    for j, cell in enumerate(cells):
        print(f"  Row {i} Col {j}: {repr(cell)}")
