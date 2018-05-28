#coding=utf-8
movies = ["The Holy Grail","The Life of Brain","The Meaning of Life"]
#向列表插入年份
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print(movies)
movies2 = ['The Holy Grail', 1975, 'The Life of Brain', 1979, 'The Meaning of Life', 1983]
print(movies2)

for i in movies2:
    print (i)