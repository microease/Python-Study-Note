# 给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。
# 例如a="cagy", b=3,
# 则输出 ：fdjb
a = "cagy"
b = 3
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 's', 'y', 'z']
list = []
for i in a:
    c = letter[(letter.index(i)+b)%26]
    # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
    list.append(c)
print("".join(map(str,list)))
