from pymysql import *


def main():
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')


if __name__ == '__main__':
    main()
