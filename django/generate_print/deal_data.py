import pandas as pd
import os




data_filter = ['订单号', '收件人姓名', '收件人地址', '收件人手机', '期望送达时间', '买家备注', '订单实际支付金额', '商家备注']




def get_data(filename):
    data = pd.read_excel(filename)
    return data
# print(data)
# print(type(data))
# print(data[filter])
# print(data.values)
# print(data.index)
# print(data.columns.tolist())


# def generate_filter(data):
#     order_dict = dict()
#     index_col = data.columns.tolist()  # 打印属性名称
#     # print(index_col)
#     final_filter = []
#
#     for i in index_col:
#         if i in data_filter:
#             final_filter.append(i)
#         elif "商品名称" in i:
#             final_filter.append(i)
#         elif "商品数量" in i:
#             final_filter.append(i)
#
#     # print(final_filter)
#     # print(data[final_filter])
#     # print(data[final_filter]['收件人姓名'][1])
#     return final_filter
def generate_order(data, order_dict, order_count):
    # print(data)
    index_col = data.index.tolist()
    # print(index_col)
    pre_dict = data[data_filter].to_dict()
    pre_dict['商品名称'] = []
    pre_dict['商品属性'] = []
    pre_dict['商品数量'] = []
    count = 1
    name_str = '商品名称-'
    att_str = '商品属性-'
    num_str = '商品数量-'
    while True:
        # print(name_str+str(count))
        # print('商品名称-1')
        # print(index_col)
        if name_str+str(count) in index_col and data[name_str+str(count)] == data[name_str+str(count)]:
            # print(type(data[name_str+str(count)]))
            pre_dict['商品名称'].append(data[name_str+str(count)])
            if data[att_str + str(count)] == data[att_str + str(count)]:
                # print(data[att_str + str(count)])
                pre_dict['商品属性'].append(data[att_str + str(count)])
            if data[num_str + str(count)] == data[num_str + str(count)]:
                # print(data[num_str + str(count)])
                pre_dict['商品数量'].append(data[num_str + str(count)])
            count = count + 1
        else:
            break
    # print(count)
    # print(pre_dict['期望送达时间'].to_pydatetime())
    pre_dict['期望送达时间'] = str(pre_dict['期望送达时间'].to_pydatetime())
    # print(pre_dict)
    order_dict[order_count] = pre_dict
    order_count = order_count + 1



def deal_data(file_name):

    order_dict = dict()
    data = get_data(file_name)
    # print(data)
    # print(data.iloc[0])
    # print(len(data))
    order_count = 0
    for index in range(len(data)):
        # print(data.iloc[index])
        generate_order(data.iloc[index], order_dict, order_count)
    # print(order_dict)
    return order_dict



