import math


def extend_gcd(a, b):
    r0, r1 = a, b
    q = math.floor(a/b)
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while r1 != 0:
        q = math.floor(r0 / r1)
        r0, r1 = r1, r0 % r1
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1

    return x0, y0, r0


if __name__ == '__main__':
    while True:  # 便于执行多组数据
        a = int(input("请输入第1个数："))
        b = int(input("请输入第2个数："))

        x, y, d = extend_gcd(a, b)
        print("最大公约数为：", d)

        # 对负数加括号
        if x < 0:
            x = "("+str(x)+")"
            y = str(y)
        elif y < 0:
            y = "("+str(y)+")"
            x = str(x)

        print("式子求解为："+str(a)+"*"+x+"+"+str(b)+"*"+y+"="+str(d))

        # 根据公约数判断是否互素
        if d==1:
            print("%d和%d互素"%(a, b))
        else:
            print("%d和%d不互素" % (a, b))