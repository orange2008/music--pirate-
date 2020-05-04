import os
import sys
while True:
    try:
        url = input("Link: ")
        saveas = input("Save as: ")
        query = 'wget -O "' + saveas + '" --no-check-certificate ' + url
        print(query)
        os.system(query)
        print("Complete.")
    except KeyboardInterrupt:
        print("Quitting..")
        sys.exit(0)


