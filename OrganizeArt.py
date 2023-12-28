import base64
from datetime import datetime
import os
import sys

### TwitterIDToTimestamp() #####################################################
def TwitterIDToTimestamp(twitterID):
    
    padding = "=" * (len(twitterID) % 4)
    twitterID += padding

    snowflakeBytes = base64.urlsafe_b64decode(twitterID)
    unixTime = int(snowflakeBytes.hex()[:16], 16)

    twitterEpoch = 1288834974657
    return ((unixTime >> 22) + twitterEpoch) / 1000

### main() ####################################################################
if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
    print(f"usage: python {sys.argv[0]} directory") ; exit(0)

for file in os.scandir(sys.argv[1]):

    if len(file.name) > 15 and file.name[15] == ".":

        unixTime = TwitterIDToTimestamp(file.name.split(".")[0])

        try:
            os.utime(file.path, (unixTime, unixTime))
            print(f"{file.name} -> {datetime.fromtimestamp(unixTime)}")
        except:
            print(f"{file.name} -> Failed to update time!")
