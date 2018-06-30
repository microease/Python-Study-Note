# 银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
# 在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万
# 以下的例子示范了阿拉伯数字到人民币大写的转换规则：
# 1	壹圆
# 11	壹拾壹圆
# 111	壹佰壹拾壹圆
# 101	壹佰零壹圆
# -1000	负壹仟圆
# 1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆
# 现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.
# 例如：a=1
# 则输出：壹圆
# 注意：请以Unicode的形式输出答案。提示：所有的中文字符，在代码中直接使用其Unicode的形式即可满足要求，中文的Unicode编码可以通过如下方式获得：u'壹'。
# 注意：代码无需声明编码！！不要在代码头部声明文件编码，否则会导致语法错误！
# Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
bigFormat = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
digit = [u'圆', u'拾', u'佰', u'仟', u'万', u'拾', u'佰', u'仟']
z = [(u'零仟', u'零佰', u'零拾', u'零零零', u'零零', u'零万', u'零圆'), (u'零', u'零', u'零', u'零', u'零', u'万', u'圆')]
print(u'零佰')