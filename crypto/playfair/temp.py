import re
import time

def generate_alpha(keyword):
    alpha_matrix = []
    
    for i in keyword:
        if i not in alpha_matrix:
            alpha_matrix.append(i)
    
    for i in range(ord('a'),ord('z')+1):
        if i == ord('j'):
            i += 1
        if i not in alpha_matrix:
            alpha_matrix.append(i)
    
    return alpha_matrix


def origin_clean(origin_text):
    for i in range(len(origin_text)-1):
        if origin_text[i] == origin_text[i+1]:
            origin_text.insert(i+1,ord('x'))
    
    if len(origin_text)%2 != 0:
        origin_text.append(ord('x'))
            
def encode(origin_text,alpha_matrix):
    startencode = time.time()  # 记录加密开始运行时间
    encode_text = []
    while len(origin_text)!=0:
        num_couple = (origin_text.pop(0),origin_text.pop(0))
        num_position1 = ((alpha_matrix.index(num_couple[0]))//5,
                         (alpha_matrix.index(num_couple[0]))%5) 
        # 第1个数的坐标(行,列 )
        num_position2 = ((alpha_matrix.index(num_couple[1]))//5,
                         (alpha_matrix.index(num_couple[1]))%5) 
        # 第2个数的坐标(行,列 )
        print(chr(num_couple[0]),chr(num_couple[1]))
        print(num_position1,num_position2)
        
        if num_position1[0]==num_position2[0]:
            #  同一行 
            encode_text.append(num_position1[0]*5+(num_position1[1]+1)%5)
            encode_text.append(num_position2[0]*5+(num_position2[1]+1)%5)
        
        elif num_position1[1] == num_position2[1]:
            # 同一列
            encode_text.append(((num_position1[0]+1)%5)*5+num_position1[1])
            encode_text.append(((num_position2[0]+1)%5)*5+num_position2[1])
                          
        else:
            # 不同行 ，不同列
            encode_text.append(num_position1[0]*5+num_position2[1])
            encode_text.append(num_position2[0]*5+num_position1[1])
    
    print(encode_text)
    encode_text = [alpha_matrix[i] for i in encode_text]
    endencode = time.time()  # 记录加密结束时间
    print("加密时间为：",endencode-startencode)
    return encode_text

def decode(encode_txt,alpha_matrix):
    startdecode = time.time()  # 记录解密开始运行时间
    en_text = encode_txt
    decode_text = []
    while len(en_text)!=0:
        num_couple = (en_text.pop(0),en_text.pop(0))
        num_position1 = ((alpha_matrix.index(num_couple[0]))//5,
                         (alpha_matrix.index(num_couple[0]))%5) 
        # 第1个数的坐标(行,列 )
        num_position2 = ((alpha_matrix.index(num_couple[1]))//5,
                         (alpha_matrix.index(num_couple[1]))%5) 
        # 第2个数的坐标(行,列 )
        print(chr(num_couple[0]),chr(num_couple[1]))
        print(num_position1,num_position2)
        
        if num_position1[0]==num_position2[0]:
            #  同一行 
            decode_text.append(num_position1[0]*5+(num_position1[1]-1)%5)
            decode_text.append(num_position2[0]*5+(num_position2[1]-1)%5)
        
        elif num_position1[1] == num_position2[1]:
            # 同一列
            decode_text.append(((num_position1[0]-1)%5)*5+num_position1[1])
            decode_text.append(((num_position2[0]-1)%5)*5+num_position2[1])
                          
        else:
            # 不同行 ，不同列
            decode_text.append(num_position1[0]*5+num_position2[1])
            decode_text.append(num_position2[0]*5+num_position1[1])
        
    decode_text = [alpha_matrix[i] for i in decode_text]
    enddecode = time.time()  # 记录解密结束时间    
    print("加密时间为：",enddecode-startdecode)    
    return decode_text

if __name__ == '__main__':
    
    while True:
    
        starttime = time.time()  # 记录程序开始时间
        keyword = [ord(x) for x in input("请输入密钥：").lower()]
        #  去除密钥中的j，将其变为i
        while ord('j') in keyword:
            keyword[keyword.index(ord('j'))] = ord('i')
        keyword = list(set(keyword))
        # 将列表转化为集合再转换为列表，从而去除重复元素
        
        
        origin_text = input("请输入明文：").lower()
        origin_text = "".join(re.findall(r'[A-Za-z]', origin_text))  # 提取字母
        origin_text = [ord(x) for x in origin_text.lower()]  # 小写并转化为ASCII码
        #  去除明文中的j，将其变为i
        while ord('j') in origin_text:
            origin_text[origin_text.index(ord('j'))] = ord('i')
        
        alpha_matrix = generate_alpha(keyword)
    
        print("密钥为：","".join([chr(x) for x in keyword]))
        print("明文为：","".join([chr(x) for x in origin_text]))
    
        print("密钥表为：","".join([chr(x)+" " for x in alpha_matrix]))
        
        origin_clean(origin_text)
        encode_text = encode(origin_text,alpha_matrix)
        print("加密后为：","".join([chr(x) for x in encode_text]))
        
        decode_text = decode(encode_text,alpha_matrix)
        print("解密后为：","".join([chr(x) for x in decode_text]))
    
        endtime = time.time()
        # 记录程序结束时间
        print("playfair加密解密运行结束！运行时间为：",endtime-starttime)
        
    
    
    
    
    
    

    
    
    '''
    alpha_matrix = [[],[],[],[],[]]
    for i in alpha_matrix:
        for j in range(5):
            if count_flag > len(keyword)-1:
                if ord('a')+count_alpha == ord('j'):
                    count_alpha += 1

                while ord('a')+count_alpha in keyword:
                    count_alpha = count_alpha +1

                i.append(ord('a')+count_alpha)

                count_alpha += 1
            else:
                i.append(keyword[count_flag])
                count_flag += 1

    print(alpha_matrix)
    '''
    



