import os
from datetime import datetime

shutdown = int(input('输入：0 定时关机，1 取消定时\n'))

if shutdown:
   os.system('shutdown -a')
   os._exit(0)

t = input('请输入关机时间，格式：时:分:秒\n')
hms = t.split(':') if ':' in t else t.split('：')

h, m, s = hms # 目标时间
h = min(int(h), 24)
m = min(int(m), 59)
s = min(int(s), 59)

now = datetime.now() # 当前时间
nh, nm, ns = now.hour, now.minute, now.second

counter = (h - nh) * 60 * 60 + (m - nm) * 60 + (s - ns) # 时间差（单位：秒）

os.system('shutdown -s -t {}'.format(counter))
os._exit(0)