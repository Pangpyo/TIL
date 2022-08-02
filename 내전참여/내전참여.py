
f = open('내전참여리스트.txt', 'r')

n = 0
playlist = []
while 1 :
    line = f.readline()
    playlist.append(line)
    if not line : break
    n += 1
f.close()

playerlist = []
for i in range(len(playlist)) :
    if i%3 == 0 :
        playerlist.append(playlist[i][0:3])

playerdic = {}
for i in playerlist :
    if i in playerdic :
        playerdic[i] += 1
    else :
        playerdic[i] = 1


f = open('내전참여횟수.txt','w')
for i,v in playerdic.items() :
    print(i,v)

f = open('내전참여.txt', 'w')
for i in playerlist :
    f.write(i)
    f.write('\n')
f.close()