import csv
import sys


fileCsv = str(sys.argv[1])
handler = open(fileCsv)
reader = csv.reader(handler)
data = list(reader)
handler.close()
print(data)

output = open('result.tsv', 'w')
outputWriter = csv.writer(output, delimiter ='\t')
for row in data:
    outputWriter.writerow(row)
output.close()
