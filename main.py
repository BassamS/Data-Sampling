import csv
from io import StringIO
import requests
import pandas as pd

file_url = 'https://data.sfgov.org/api/views/vw6y-z8j6/rows.csv?accessType=DOWNLOAD'
counter = 1000
lines = []

response = requests.get(file_url, stream=True)

for index, line_record in enumerate(response.iter_lines(chunk_size=1024)):
    if index > counter:
        break
    line_decoded = line_record.decode('utf-8')
    f = StringIO(line_decoded)
    reader = csv.reader(f, delimiter=',', quotechar='"')
    lines.append(next(reader))

df = pd.DataFrame(data=lines[1:], columns=lines[0])
print(df.to_csv('sample dataset.csv'))
