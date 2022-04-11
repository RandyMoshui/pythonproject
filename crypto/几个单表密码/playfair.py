def generate_alpha(keyword):
    alpha_matrix = []

    for i in keyword:
        if i not in alpha_matrix:
            alpha_matrix.append(i)

    for i in range(ord('a'), ord('z') + 1):
        if i == 'j':
            i += 1
        if i not in alpha_matrix:
            alpha_matrix.append(i)

    return alpha_matrix


def origin_clean(origin_text):
    for i in range(len(origin_text) - 1):
        if origin_text[i] == origin_text[i + 1]:
            origin_text.insert(i + 1, ord('x'))

    if len(origin_text) % 2 != 0:
        origin_text.append(ord('x'))


def encode(origin_text, alpha_matrix):
    encode_text = []
    while len(origin_text) != 0:
        num_couple = (origin_text.pop(0), origin_text.pop(0))
        num_position1 = ((alpha_matrix.index(num_couple[0]) + 1) // 5,
                         (alpha_matrix.index(num_couple[0]) + 1) % 5)
        # 第1个数的坐标(行,列 )
        num_position2 = ((alpha_matrix.index(num_couple[1]) + 1) // 5,
                         (alpha_matrix.index(num_couple[1]) + 1) % 5)
        # 第2个数的坐标(行,列 )

        if num_position1[0] == num_position2[0]:
            #  同一行
            encode_text.append(num_position1[0] * 5 + (num_position1[1] + 1) % 5)
            encode_text.append(num_position2[0] * 5 + (num_position2[1] + 1) % 5)

        elif num_position1[1] == num_position2[1]:
            # 同一列
            encode_text.append(((num_position1[0] + 1) % 5) * 5 + num_position1[1])
            encode_text.append(((num_position2[0] + 1) % 5) * 5 + num_position2[1])

        else:
            # 不同行 ，不同列
            encode_text.append(num_position1[0] * 5 + num_position2[1])
            encode_text.append(num_position2[0] * 5 + num_position1[1])

    print(encode_text)
    encode_text = [alpha_matrix[i] for i in encode_text]

    return encode_text


if __name__ == '__main__':
    keyword = [ord(x) for x in input("请输入密钥：").lower()]
    origin_text = [ord(x) for x in input("请输入明文")]

    alpha_matrix = generate_alpha(keyword)

    print(alpha_matrix)
    origin_clean(origin_text)
    encode_text = encode(origin_text, alpha_matrix)
    encode_text = [chr(x) for x in encode_text]
    print("加密后为：", "".join(encode_text))

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




