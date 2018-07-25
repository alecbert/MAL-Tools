import re

file = open("PastebinStatus.txt","r")
lineReader = file.readlines()
epsLeft = 0

#find the counting portion of each line and figure out progress vs episodes left
for line in lineReader:
        match = re.search("\d+\/\d+", line)
        if match:
            epInfo = match.group(0).split('/')
            epsLeft += int(epInfo[1]) - int(epInfo[0])
            
print(epsLeft)