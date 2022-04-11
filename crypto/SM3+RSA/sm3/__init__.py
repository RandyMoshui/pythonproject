import cal_support

IV = '1110011100000000001011001101111010010010001010010110010101110010001011100100100010000101101011111011010100010100000011000000000101010010110111100110000101111000001011000110001001110001010101011100011100011011110111001001101101100001111101100001110010011101'

# SM3杂凑算法
# 主要用于数字签名及认证、消息认证码生成及验证、随机数生成
# 安全性与SHA-256相当


def generate(i):
    # Tj常量
    if 0 <= i <= 15:
        Tj = bin(0x79cc4519)[2:]
    elif 15 <= i <= 63:
        Tj = bin(0x7a879d8a)[2:]
    return Tj


def p(i, x):
    # 置换函数
    # i为int类型，x为str类型
    if i == 0:
        return cal_support.function_xor(cal_support.function_xor(x
                                        , cal_support.left_shift(x, 9))
                                        , cal_support.left_shift(x, 17))
    elif i == 1:
        return cal_support.function_xor(cal_support.function_xor(x
                                                                 , cal_support.left_shift(x, 15))
                                        , cal_support.left_shift(x, 23))
    else:
        print("置换函数参数传入有误，i为", i)
        exit()


def function_FF(x, y, z, i):
    # 布尔函数FF
    # x,y,z为str类型 i为int类型
    if 0 <= i <= 15:
        return cal_support.function_xor(x,cal_support.function_xor(y, z))
    elif 16 <= i <= 63:
        return cal_support.function_or(cal_support.function_and(x, y)
                                       , cal_support.function_or(
                                             cal_support.function_and(x, y),
                                             cal_support.function_and(y, z)
                                         ))
    else:
        print("function_FF()传入i出错，i为", i)
        exit()


def function_GG(x, y, z, i):
    # 布尔函数GG
    # x,y,z为str类型 i为int类型
    if 0 <= i <= 15:
        return cal_support.function_xor(x, cal_support.function_xor(y, z))
    elif 16 <= i <= 63:
        return cal_support.function_or(cal_support.function_and(x, y),
                                             cal_support.function_and(
                                                 cal_support.function_no(x),
                                                                          z)
                                         )
    else:
        print("function_GG()传入i出错，i为", i)
        exit()


def turn_to_bits(message):
    # 将消息转换为字符串，并填充

    middle_message = [bin(ord('i'))[2:] for i in message]
    middle_message = "".join(middle_message)

    length = bin(len(middle_message))[2:]
    while len(length) < 64:
        length = '0' + length
    else:
        length = length[-64:]

    # 字符串填充，1+‘0’*k
    middle_message = middle_message + '1'
    while len(middle_message) % 512 != 448:
        middle_message = middle_message + '0'

    middle_message = middle_message + length

    return middle_message
    # middle_message为字符串类型


def information_addition(b):
    # 消息拓展函数，b为str类型
    # w1,w2为字符串数组类型,为拓展后的字分组
    w1 = [b[i:i+32] for i in range(0,512,32)]
    w2 = []

    for i in range(16, 68):
        w1.append(
            cal_support.function_xor(p(1
                                       , cal_support.function_xor(
                    w1[i-16], cal_support.function_xor(
                        w1[i-9], cal_support.function_xor(
                            cal_support.left_shift(w1[i-3], 15)
                            , cal_support.left_shift(w1[i-13], 7)
                        )
                    )
                ))
                                     , w1[i-6]))

    for i in range(0, 64):
        w2.append(cal_support.function_xor(w1[i], w1[i+4]))

    return w1, w2


def CF(v, b):
    # 压缩函数, v,b为str类型，b为长度为512的消息分组
    w1, w2 = information_addition(b)
    A, B, C, D, E, F, G, H = v[0:32], v[32:64], v[64:96], v[96:128], v[128:160]\
        , v[160:192], v[192:224], v[224:256]  # A,B,C,D,E,F,G,H为str类型
    for i in range(0, 64):
        ss1 = cal_support.left_shift(cal_support.str_and(cal_support.str_and(cal_support.left_shift(A, 12), E)
                                                         , cal_support.left_shift(generate(i), i)), 7)
        ss2 = cal_support.function_xor(ss1, cal_support.left_shift(A, 12))
        tt1 = cal_support.str_and(cal_support.str_and(cal_support.str_and(
            cal_support.str_and(function_FF(A, B, C, i), D), D), ss2), w2[i])
        tt2 = cal_support.str_and(cal_support.str_and(cal_support.str_and(function_GG(E, F, G, i), H),
                                  ss1), w1[i])
        D = C
        C = cal_support.left_shift(B, 9)
        B = A
        A = tt1
        H = cal_support.left_shift(F, 19)
        F = E
        E = p(0, tt2)

    return cal_support.function_xor(A+B+C+D+E+F+G+H, v)


def iteration(bits):
    # sm3迭代过程
    # bits为字符串类型
    V = [IV]
    B = [bits[i:i+512] for i in range(0, len(bits), 512)]
    for i in range(0, len(B)):
        V.append(CF(V[i], B[i]))
    return V[-1][-256:]
