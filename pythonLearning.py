#TempConvert.py
TempStr = input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

    '''
    1.列表的索引切片
        从前往后的索引是0,1，。。。
        从后往前的索引是-1，-2，。。。
    2.输入一般用input()函数，括号里面的内容是提示，python统一将输入的内容看成字符串，所以有需要的可以再进行整数转换
    3.评估函数eval()：去掉参数最外侧引号并执行余下的语句
    4.格式化.format(F)，将变量F填充到前面字符串里面的{:.2f}中，保留两位小数 
