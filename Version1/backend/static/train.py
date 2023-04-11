import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch import optim
from NetComponents import ChessValueDataset
from NetComponents import Net
from torch import cuda

if __name__ == "__main__":
    device = "cuda"

    chessDataset = ChessValueDataset()
    trainLoader = torch.utils.data.DataLoader(chessDataset, batch_size=256, shuffle=True)
    model = Net()
    optimizer = optim.Adam(model.parameters())
    floss = nn.MSELoss()

    if device == "cuda":
        model.cuda()

    model.train()
    #100
    for epoch in range(2000):
        allLoss = 0
        numLoss = 0
        for batchIdx, (data, target) in enumerate(trainLoader):
            target = target.unsqueeze(-1)
            data, target = data.to(device), target.to(device)
            data = data.float()
            target = target.float()

            optimizer.zero_grad()
            output = model(data)

            loss = floss(output, target)
            loss.backward()
            optimizer.step()
            
            allLoss += loss.item()
            numLoss += 1

        print("%3d: %f" % (epoch, allLoss/numLoss))
        torch.save(model.state_dict(), "nets/value.pth")