import torch

def acc(predict, target):
    predict = torch.argmax(predict,dim=1)#找到概率最大的类
    correct = (predict == target).sum()
    return correct
