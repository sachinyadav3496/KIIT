import os
import time
seconds = 10*60
for i in range(seconds+1):
    os.system('cls')
    print("\n\n\n\n\n\n")
    print(f"Time Left in Break: {seconds-i} seconds".center(100))
    time.sleep(1)
