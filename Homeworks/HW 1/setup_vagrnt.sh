#! /bin/bash
#

CPUTEST_PATH="C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test1.sh"
FILEIOTEST_PATH="C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test2.sh"
MEMORYTEST_PATH="C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test3.sh"

sudo apt-get update
sudo apt-get install -y sysbench
chmod +x "C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test1.sh"
chmod +x "C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test2.sh"
chmod +x "C:\Users\tsaur\OneDrive\Desktop\CSEN241_CC\Homeworks\HW 1\test3.sh"

"$CPUTEST_PATH"
"$FILEIOTEST_PATH"
"$MEMORYTEST_PATH"