import torch
from dateprocess import getdata
from torch.utils.data import random_split
from model import tranfomerModel
import numpy as np
from metric import acc

def train():
    batchSize = 32
    learningRate = 0.001
    numHeads = 4
    numTokens = 88
    numLayers = 12
    hiddenSize = 64
    numClasses = 18
    numEpochs = 8
    length = 20

    data, label = getdata()
    data = np.array(data)
    label = np.array(label)
    number = len(data)
    indices = list(range(number))  # 标号
    np.random.shuffle(indices)  # 打乱
    # traindata, testdata = random_split(data, [int(number*0.8), number-int(number*0.8)])
    traindata = data[indices[:int(number * 0.8)]]
    trainlabel = label[indices[:int(number * 0.8)]]
    testdata = data[indices[int(number * 0.8):]]
    testlabel = label[indices[int(number * 0.8):]]
    # print(len(testdata))
    traindata = torch.tensor(traindata, dtype=torch.long)
    trainlabel = torch.tensor(trainlabel, dtype=torch.long)
    testdata = torch.tensor(testdata, dtype=torch.long)
    testlabel = torch.tensor(testlabel, dtype=torch.long)

    model = tranfomerModel(numTokens, numHeads, numLayers, hiddenSize, numClasses, length)

    optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

    lossFunction = torch.nn.CrossEntropyLoss()

    device = torch.device("cuda")
    model = model.to(device)

    for i in range(numEpochs):
        numBatches = int(int(number * 0.8) / batchSize)
        loss_epoch = 0
        accuracy = 0
        for j in range(numBatches):
            data = traindata[j * batchSize:(j + 1) * batchSize]
            label = trainlabel[j * batchSize:(j + 1) * batchSize]
            data = data.t()
            data = data.to(device)
            label = label.to(device)
            # print(data.shape)
            output = model(data)  # 这里调用的是forward函数 继承了torch.nn类
            loss = lossFunction(output, label)
            cor = acc(output, label)
            accuracy += cor
            loss_epoch += loss
            optimizer.zero_grad()  # 梯度清零
            loss.backward()
            optimizer.step()  # 模型更新
        print("epch:", i, "loss", loss_epoch / (j + 1))
        print("epch:", i, "accuracy", accuracy / (j + 1) / batchSize)
        torch.save(model, "model.pt")

        if i % 5 == 0:
            numBatches = int(len(testdata) / batchSize)
            for j in range(numBatches):
                data = testdata[j * batchSize:(j + 1) * batchSize]
                label = testlabel[j * batchSize:(j + 1) * batchSize]
                data = data.t()
                data = data.to(device)
                output = model(data)
                label = label.to(device)
                cor = acc(output, label)
                accuracy += cor

            print("test accuracy", accuracy / (j + 1) / batchSize)


