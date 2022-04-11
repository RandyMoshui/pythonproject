import argparse
import RSA
import sm3

parser = argparse.ArgumentParser()
parser.add_argument('-M', type=str, default='input', metavar='Method', help='设置加密模式，file为文件，input为输入字符串')
parser.add_argument('-P', type=str, default='mingwen.txt', metavar='file_path', help='文件路径')
parser.add_argument('-S', type=str, default="201983290527zjh", metavar='String', help='读入字符串')
parser.add_argument('-R', type=bool, default=False, metavar="RSA", help="是否启用RSA")
args = parser.parse_args()
print(args.P)
print(args.R)

def rsa_encode_main(str):
    public_key, private_key = RSA.generate_key()
    encode_str = RSA.rsa_encode(str, public_key)
    return encode_str


if __name__ == '__main__':
    if args.M == 'file':
        file = open(args.P)
        message = file.read()
    elif args.M == 'input':
        message = args.S
    else:
        print("模式选择输入有误！默认使用input")
        message = args.S
    bits_message = sm3.turn_to_bits(message)
    print("经过SM3加密后的比特流为：", sm3.iteration(bits_message))

    if args.R == True:
        print("RSA已被启用，正在执行RSA加密")
        data = sm3.iteration(bits_message)
        print("经过RSA加密后的数据为：", rsa_encode_main(data))
    # print(cal_support.left_shift('10000101516551',12))

