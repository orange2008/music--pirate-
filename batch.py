import os
import sys
import json
print("Processing..")
with open("queue.json") as fp:
    ff = json.load(fp)

count = 0
for url, saveas in ff.items():
    print(url + " -> "+ saveas)
    query = 'wget -O "' + saveas + '" --no-check-certificate ' + url
    print(query)
    os.system(query)
    count += 1

print("\n\n\n Completed. Total: " + str(count))
