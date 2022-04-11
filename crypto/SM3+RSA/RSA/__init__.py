import random
import math

key_length = 1024


def fast_mod(b, n, m):
    """
    快速幂
    """
    ret = 1
    tmp = b
    while n:
        if n & 0x1:
            ret = ret * tmp % m
        tmp = tmp * tmp % m
        n >>= 1
    return ret


#Miller-Rabin
def prime_test(n):
        """
        测试n是否为素数
        """
        q = n - 1
        k = 0
        # 寻找k,q 是否满足2^k*q =n - 1
        while q % 2 == 0:
            k += 1
            q = q // 2
        a = random.randint(2, n - 2)
        # 如果 a^q mod n= 1, n 可能是一个素数
        if fast_mod(a, q, n) == 1:
            return True
        # 如果存在j满足 a ^ ((2 ^ j) * q) mod n == n-1, n 可能是一个素数
        for j in range(0, k):
            if fast_mod(a, (2 ** j) * q, n) == n - 1:
                return True
        # n 不是素数
        return False


def random_prime(half_len):
    while True:
        n = random.randint(0, 1 << half_len)#求2^half_len之间的大数
        if n % 2 != 0:
            found = True
            # 随机性测试
            for i in range(0, 5):   #5的时候错误率已经小于千分之一
                if prime_test(n) == False:
                    found = False
                    break
            if found == True:
                return n



def generate_num():
    num1 = random_prime(key_length//2)
    num2 = random_prime(key_length//2)
    while num1 == num2:
        num2 = random_prime(key_length//2)
    return num1, num2


def judge(a,b):
    while b != 0:
        a, b = b, a%b
        if a == 1:
            return True
        else:
            return False


def ext_gcd(a, b): #扩展欧几里得算法
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_gcd(b, a % b) #递归直至余数等于0(需多递归一层用来判断)
        x, y = y, (x - (a // b) * y) #辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立
        return x, y, gcd


def generate_key():
    p, q = generate_num()
    n = p * q
    fi_n = (p-1)*(q-1)

    # e = random.randint(1, fi_n)
    # while judge(e, fi_n) is False:
    #    e = random.randint(1, fi_n)

    e = 65537  # 节约时间取固定值
    (x, d, z) = ext_gcd(e, fi_n)
    if d < 0:
        d = d + fi_n
    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def rsa_encode(str, public_key):
    # public_key, ans = generate_key()
    n, e = public_key
    ans = ""
    num_str = [(ord(x)**e) % n for x in list(str)]
    return num_str


def rsa_decode(num_str, private_key):
    # ans, private_key = generate_key()
    n, d = private_key
    str = [(pow(c, d, n)) for c in num_str]
    print(str[0])
    return str


'''
if __name__ == '__main__':
    str = input("请输入待加密字符串：")
    print("加密前长度为：", len(str))
    print("加密前内容:", str)
    public_key, private_key = generate_key()
    print("公钥为：", public_key)
    print("正在加密：")
    encode_str = rsa_encode(str, public_key)
    print("私钥为：", private_key)
    print("正在解密:")
    decode_str = rsa_decode(encode_str, private_key)
    print("加密后内容为：", encode_str)
    print("解密后内容为：", decode_str)
    '''
