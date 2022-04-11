import matplotlib.pyplot as plt
import re

passwd = {
    'a': 'k', 'b': 'z', 'c': 'm', 'd': 'j',
    'e': 'l', 'f': 'a', 'g': 'w', 'h': 'b',
    'i': 'p', 'j': 'd', 'k': 'y', 'l': 'z',
    'm': 'e', 'n': 't', 'o': 'i', 'p': 'o',
    'q': 'c', 'r': 'h', 's': 'n', 't': 'q',
    'u': 'r', 'v': 's', 'w': 'u', 'x': 'v',
    'y': 'x', 'z': 'f'
}
# a b c d e f g h i j k l m n o p q r s t u w


def strcount(str):
    alpha_statistic = []

    for x in [chr(i+97) for i in range(0, 26)]:
        alpha_statistic.append(str.count(x) / len(str))
    return alpha_statistic

def attack(str):
    alpha_statistic = strcount(str)
    know_statistic = [0.08167, 0.01492, 0.02782, 0.04253, 0.012702, 0.02228, 0.02015, 0.06094, 0.06996, 0.00153,
                      0.00772,
                      0.04025, 0.02406, 0.06749, 0.07507, 0.01928, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                      0.00978, 0.02360, 0.00150, 0.001974, 0.00074]
    plt.subplot(211)
    plt.plot(alpha_statistic)
    plt.title("密文统计学分析")


    plt.subplot(212)
    plt.plot(know_statistic)
    plt.title("已知统计学特征")

if __name__ == '__main__':
    str = input("请输入英文字符串：")
    str = "".join(re.findall(r'[A-Za-z]', str))
    print(str)
    str = str.lower()  # 变为小写以便处理
    str_encode = [passwd[x] for x in str]
    str_encode = "".join(str_encode)
    print(str_encode)
    print(strcount(str_encode))
    print(attack(str_encode))