# 给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
# 回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
a = "abcba"
n = 2
a1 = a[::-1]
flag = "NO"
for i in range(0, len(a) - n - 1):
    s = a[i:i + n]
    if (s in a1):
        flag = "YES"
        break;
print(flag)