# coding=utf-8
from sys import argv

script, user_name = argv
prompt = '> '
print("Hi %s,I'm the %s script." % (user_name, script))
print("我想问几个问题")
print("你喜欢我吗？%s" % user_name)
likes = input(prompt)
print("Where do you live, %s?" % user_name)
lives = input(prompt)
print("你喜欢哪种电脑？")
computer = input(prompt)
print("""
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
