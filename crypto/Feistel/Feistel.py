import sys
sys.setrecursionlimit(1000000000)

encode_str = []
decode_str = []

def convert2num(str):
    num_str = [ord(x) for x in str]
    if len(num_str) % 2 != 0:
        num_str.append(10)  # 若长度不为2的倍数在末尾加换行符填充

    return num_str


def xor_list(num_str1, num_str2):
    num_str3=[]
    for i in range(0, len(num_str1)):
        num_str3.append(num_str1[i] ^ num_str2[i])  # 异或运算
    return num_str3


def function_F(num_str, key):
    # F函数设计为简单的异或，即每个元素与密钥key进行异或操作
    return [x ^ key for x in num_str]

def feistel_encode(num_str, round, key):
    # str为待加密字符串， round为轮数, key为F函数的密钥
    global encode_str
    if round == 0:
        encode_str = num_str
        return
    else:
        num_left = num_str[0:len(num_str)//2]
        num_right = num_str[len(num_str)//2:]

        num_left = xor_list(num_left, function_F(num_right, key))
        num_str = num_right + num_left
        # print(33 - round, "加密轮", num_str)
        feistel_encode(num_str, round-1, key)

def feistel_decode(num_str,round,key):
    global decode_str
    if round == 0:
        num_left = num_str[0:len(num_str) // 2]
        num_right = num_str[len(num_str) // 2:]
        num_str = num_right + xor_list(num_left, function_F(num_right, key))
        num_left = num_str[0:len(num_str) // 2]
        num_right = num_str[len(num_str) // 2:]
        num_str = num_right + xor_list(num_left, function_F(num_right, key))
        decode_str = num_str
        return
    else:
        num_left = num_str[0:len(num_str) // 2]
        num_right = num_str[len(num_str) // 2:]

        num_str = num_right + xor_list(num_left, function_F(num_right, key))
        # print(33-round,"解密轮",num_str)
        feistel_decode(num_str, round-1, key)

if __name__ == '__main__':
    str = input("请输入待加密字符串：")
    num_str = convert2num(str)
    print("代加密字符串：",num_str)
    #print(xor_list(num_str[:len(num_str)//2], num_str[len(num_str)//2:len(num_str)]))
    feistel_encode(num_str, 32, 64)
    print("加密后字符串为：", encode_str)
    feistel_decode(encode_str, 32, 64)
    print("解密后字符串为：", decode_str)
    decode_str2 = [chr(x) for x in decode_str]
    print("解密数组转换为字母后为", "".join(decode_str2))
