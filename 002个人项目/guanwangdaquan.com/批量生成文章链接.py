# https://guanwangdaquan.com/?p=62584
url = "https://guanwangdaquan.com/?p="
f = open("text.txt", 'wb')
for i in range(62585):
    print(url + str(i))
    content = url + str(i)+"\r\n"
    f.write(content.encode())
f.close()