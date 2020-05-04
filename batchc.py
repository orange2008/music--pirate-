import json
import sys
d = {}
while True:
    print("Press Ctrl+C to save and quit")
    try:
        s1 = input("URL: ")
        s2 = input("Save as: ")
        s3 = s2.lower()
        if ".mp3" in s3:
            d[s1] = s2
        else:
            s2 += ".mp3"
            d[s1] = s2
    except KeyboardInterrupt:
        print("\n\n\n Saving...")
        with open("queue.json", 'w') as fp:
            json.dump(d, fp)
            sys.exit(0)
