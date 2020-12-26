import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class NN2DMEL(nn.Module):
    def __init__(self, num_class):
        super(NN2DMEL,self).__init__()
        
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=8,kernel_size=3,stride=1)
        self.dropout1 = nn.Dropout(0.3) 
        self.conv2 = nn.Conv2d(in_channels=8,out_channels=32,kernel_size=3,stride=1)
        self.dropout2 = nn.Dropout(0.3)
        self.conv3 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3,stride=1)
        self.fc1 = nn.Linear(4224, 256)
        self.batch1= nn.BatchNorm1d(256)
        self.dropout5 = nn.Dropout(0.3)
        self.fc2 = nn.Linear(256,128)
        self.batch2= nn.BatchNorm1d(128)
        self.dropout6 = nn.Dropout(0.3)
        self.fc3 = nn.Linear(128, num_class)
        
    def forward(self, x):
        
        x = F.max_pool2d(F.relu(self.conv1(x)),kernel_size=3)
        x = self.dropout1(x)      
        x = F.max_pool2d(F.relu(self.conv2(x)),kernel_size=3)
        x = self.dropout2(x)
        x = (F.relu(self.conv3(x)))
        x = self.dropout2(x)
        x = F.relu(self.batch1(self.fc1(x.reshape(-1,x.shape[1] * x.shape[2]*x.shape[3]))))
        x = self.dropout5(x)
        x = F.relu(self.batch2(self.fc2(x)))
        x = self.dropout6(x)        
        x = self.fc3(x)
        return x 