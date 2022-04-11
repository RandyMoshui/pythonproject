
def convert2num(str):
    num_str = [ord(x) for x in str]
    if len(num_str) % 2 != 0:
        num_str.append(10)  # 若长度不为2的倍数在末尾加换行符填充

    return num_str

def xor_list(num_str1,num_str2):
    num_str3 =

def feistel_encode(num_str):



if __name__ == '__main__':
    str = input("请输入代加密字符串：")
    num_str = convert2num(str)
