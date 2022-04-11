import math

# 私钥256bit，公钥512bit
# 明文长度可以为任意值，其基本原理类似于流密码，
# 由KDF生成与明文长度一致的密钥流，与明文进行异或


def ecp(a, b, x, y,):  # 椭圆曲线（Elliptic curve）
    # p为质数，a,b应小于p且4a^3+27b^2 != (0 mod p)
    # (x,y)的负元(x,p-y)

    indepen_variable = x ** 3 + a * x + b
    if indepen_variable < 0:
        print("a,b,c,x,y取值出错，根号不可为负")
        exit()
    y = math.sqrt(indepen_variable)
    return y


def ask_rank(x, y, prime, a, b):
    # 求一点的阶
    p = (x, y)
    p_reverse = (x, prime-y)
    n_count = 0





