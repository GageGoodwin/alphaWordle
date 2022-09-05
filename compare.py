
potentialWords = []
f = open("potentialWords.txt", "r")
x = f.read()
pwordList = x.split("\n")


usedWords = []
f = open("usedWords.txt", "r")
x = f.read()
uwordList = x.split("\n")

print(len(set(uwordList)))
print(len(set(pwordList)))

count = 0
for i in pwordList:
    if i in uwordList:
       pwordList.remove(i)


print(len(set(pwordList)))