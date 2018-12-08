Rain,Song = map(int,raw_input().split())
list = [int(x) for x in raw_input().split()]
if Rain and song in list:
    print"yes"
else:
    print"no"
