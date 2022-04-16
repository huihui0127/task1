import os #读路径
import torch
import numpy as np


def getdata():
    length = 20
    data = []  # 名字 列表
    label = []  # 国家 列表
    vocab = {}  # 词典 用的字典
    vocab["pad"] = 0
    count = 1
    datatensor = []  # 记录每个名字的tensor的列表
    for i, file in enumerate(os.listdir("data/names")):
        with open("data/names/" + file) as f:  # with 会自动关闭
            lines = f.readlines()
            for line in lines:
                line = line.strip("\n")  # 去掉\n
                data.append(line)
                label.append(i)
                for s in line:
                    if s not in vocab:
                        vocab[s] = count
                        count = count + 1

    numberletters = len(vocab.keys())  # 字典长度
    #print(numberletters)

    for d in data:

        tensor = np.zeros(length)
        for i in range(length):
            if i < len(d):
                tensor[i] = vocab[d[i]]

        datatensor.append(tensor)
    #print(datatensor[0])
    return datatensor , label
#getdata()












