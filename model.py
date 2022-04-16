#分类不用decoder
import torch
from torch.nn import TransformerEncoder
from torch.nn import TransformerEncoderLayer

class tranfomerModel(torch.nn.Module):
    def __init__(self, numTokens, nHeads, numLayers, hiddenSize, numClasses,seqLen):
        super(tranfomerModel, self).__init__()#embedding也继承了module
        self.embedding = torch.nn.Embedding(numTokens, hiddenSize)
        encoderLayers = TransformerEncoderLayer(hiddenSize, nHeads)
        self.encoder = TransformerEncoder(encoderLayers, numLayers)
        self.output = torch.nn.Linear(seqLen*hiddenSize, numClasses)#全连接


    def forward(self, input):
        input = self.embedding(input)
        input = self.encoder(input)
        #print(input.shape)
        input = input.transpose(0, 1).reshape(input.shape[1],-1)#-1是还剩下的
        #print(input.shape)
        input = self.output(input)
        return input

