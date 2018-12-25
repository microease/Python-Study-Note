# 解压可迭代对象赋值给多个变量
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)


grades = 1, 2, 3, 4, 5
drop_first_last(grades)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)
