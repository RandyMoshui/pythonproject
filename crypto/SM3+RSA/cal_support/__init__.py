import math


def str_and(x, y):
    # 字符串相加
    try:
        str = []
        if len(x) == len(y):
            # print(1)
            for i in range(len(x)):
                #print("i", i, "x[i]", x[i], "y[i]", y[i])
                if x[i] == '1':
                    if y[i] == '0':
                        str.append('1')
                    elif y[i] == '1':
                        str.append('10')
                elif x[i] == '0':
                    if y[i] == '1':
                        str.append('1')
                    elif y[i] == '0':
                        str.append('0')

        elif len(x) > len(y):
            # print(2)
            diat = len(x) - len(y)
            for i in range(diat):
                str.append(x[i])

            for i in range(len(y)):
                if x[i + diat] == '1':
                    if y[i] == '0':
                        str.append('1')
                    elif y[i] == '1':
                        str.append('10')

                elif x[i+diat] == '0':
                    if y[i] == '1':
                        str.append('1')
                    elif y[i] == '0':
                        str.append('0')

        elif len(y) > len(x):
            # print(3)
            diat = len(y) - len(x)
            for i in range(diat):
                str.append(y[i])
            for i in range(len(x)):
                if x[i] == '1':
                    if y[i + diat] == '0':
                        str.append('1')
                    elif y[i + diat] == '1':
                        str.append('10')

                elif x[i] == '0':
                    if y[i + diat] == '1':
                        str.append('1')
                    elif y[i + diat] == '0':
                        str.append('0')

        # print("中间结果为", str)

        for i in range(len(str) - 1, 0, -1):
            # print("i:", i, "str", str)
            if str[i] == '10':
                if str[i - 1] == '1':
                    str[i] = '0'
                    str[i - 1] = '11'
                elif str[i - 1] == '0':
                    str[i] = '0'
                    str[i - 1] = '1'
                elif str[i - 1] == '10':
                    str[i - 1] = '11'
                    str[i] = '0'
                else:
                    print('加法器出现其他情况，错误！')

            elif str[i] == '11':
                if str[i - 1] == '1':
                    str[i] = '1'
                    str[i - 1] = '11'
                elif str[i - 1] == '0':
                    str[i] = '1'
                    str[i - 1] = '1'
                elif str[i - 1] == '10':
                    str[i - 1] = '11'
                    str[i] = '1'
                else:
                    print('加法器出现其他情况，错误！')
        return "".join(str)

    except:
        print("x is", x)
        print("y is", y)
        print("结果为：", "".join(str))
        print("字符串相加出错")


'''def function_f(x, y, z):
    # x,y,z均为int类型
    return (x & y) | ((~x) & z)


def function_g(x, y, z):
    return (x & z) | (y & (~z))


def function_h(x, y, z):
    return x ^ y ^ z


def function_i(x, y, z):
    return y ^ (x | (~ z))
'''


def function_and(x, y):
    str = []
    # 字符串与运算
    try:

        if len(x) == len(y):
            try:
                for i in range(len(x)):
                    # print("x[i]", x[i], "y[i]", y[i])
                    if x[i] == '0' or y[i] == '0':
                        str.append('0')
                    elif x[i] == '1' and y[i] == '1':
                        str.append('1')
            except:
                print("字符串与运算中等于出错！")
                exit()

        elif len(x) > len(y):
            try:
                diat = len(x) - len(y)
                for i in range(len(y)):
                    if x[diat + i] == '0' or y[i] == '0':
                        str.append('0')
                    else:
                        str.append('1')
            except:
                print("字符串与运算中>出错！")
                exit()

        elif len(y) > len(x):
            try:
                diat = len(y) - len(x)
                for i in range(len(x)):
                    if y[diat + i] == '0' or x[i] == '0':
                        str.append('0')
                    else:
                        str.append('1')
            except:
                print("字符串与运算中<出错！")
                exit()
        # print("x is", x)
        # print("y is", y)
        # print("str is", "".join(str))
        return "".join(str)
    except:
        print("x is", type(x), x)
        print("y is", type(y), y)
        print("字符串与运算出错")
        print("出错字符串为：x:", x, "y:", y)
        print(str)
        exit()



def function_or(x, y):
    str = []
    # 字符串或运算
    try:

        if len(x) == len(y):
            for i in range(len(x)):
                if x[i] == '1' or y[i] == '1':
                    str.append('1')
                else:
                    str.append('0')

        elif len(x) > len(y):
            diat = len(x) - len(y)
            for i in range(0, diat):
                str.append(x[i])
            for i in range(len(y)):
                if x[diat + i] == '1' or y[i] == '1':
                    str.append('1')
                else:
                    str.append('0')

        elif len(y) > len(x):
            diat = len(y) - len(x)

            for i in range(0, diat):
                str.append(y[i])

            for i in range(len(x)):
                if y[diat + i] == '1' or x[i] == '1':
                    str.append('1')
                else:
                    str.append('0')
        # print("或运算结果", "".join(str))
        return "".join(str)
    except:

        print("字符串或运算出错")


def function_no(x):
    # 字符串非操作
    str = []
    try:
        for i in range(len(x)):
            if x[i] == '1':
                str.append('0')
            elif x[i] == '0':
                str.append('1')
        # print("非运算结果", "".join(str))
        return "".join(str)
    except:
        print("非运算出错")


def function_xor(x, y):
    # 异或操作
    try:
        str = []
        if len(x) == len(y):
            for i in range(len(x)):
                if x[i] == y[i]:
                    str.append('0')
                elif x[i] != y[i]:
                    str.append('1')
        elif len(x) > len(y):
            diat = len(x) - len(y)
            for i in range(diat):
                str.append('1')
            for i in range(len(y)):
                if x[diat + i] == y[i]:
                    str.append('0')
                elif x[diat + i] != y[i]:
                    str.append('1')
        elif len(x) < len(y):
            diat = len(y) - len(x)
            for i in range(diat):
                str.append('1')
            for i in range(len(x)):
                if y[diat + i] == x[i]:
                    str.append('0')
                elif y[diat + i] != x[i]:
                    str.append('1')
        return "".join(str)
    except:
        print("异或出错")


def left_shift(x, y):
    # 字符串循环左移
    # x为字符串类型，y为int型
    try:
        if type(x)!= str or type(y) != int:
            raise ValueError("left_shift传入类型出错")
        middle_x = [i for i in x]
        for i in range(y):
            middle_x.append(middle_x.pop(0))
        middle_x = "".join(middle_x)
        return middle_x
    except ValueError:
        print("左移类型出错")
        print("类型为：", type(x), type(y))
        print("第一个参数为：", x, "第二个参数为：", y)
        exit()

    except:
        print("循环左移出错")




'''
if __name__ == '__main__':
    print('str_and', str_and('1001', '0100'))
    print('function_and', function_and('1001', '0100'))
    print('function_or', function_or('1001', '0100'))
    print('function_xor', function_xor('1001', '0100'))'''