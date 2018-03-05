# 自定义过滤器函数
# 1.导入必须的包
from django.template import Library

# 2.创建Library对象
register = Library()

# 3.创建过滤器函数,并用Library对象.filter装饰
# 至少有一个参数(调用过滤器的模板变量),至多有两个
# Library对象名register固定!!
@register.filter
def mod(num):
    # 判断num是否偶数
    return num % 2 == 0