import torch.nn as nn
import torch
import Config


class DQNNet(nn.Module):
    def __init__(self):
        super(DQNNet, self).__init__()
        self.n_features = Config.N_FEATURES
        self.n_actions = Config.N_ACTIONS

        self.layers = nn.Sequential(
            nn.Linear(self.n_features, self.n_features * 8),
            nn.PReLU(),
            nn.Linear(self.n_features * 8, self.n_features * 8),
            nn.PReLU()
        )
        self.value = nn.Sequential(
            nn.Linear(self.n_features * 8, self.n_features * 2),
            nn.PReLU(),
            nn.Linear(self.n_features * 2, 1)
        )

        self.advantage = nn.Linear(self.n_features * 8, self.n_actions)

    def forward(self, x):
        x = self.layers(x)
        value = self.value(x)
        advantage = self.advantage(x)
        out = value + advantage - torch.mean(advantage, dim=1, keepdim=True)
        return out

    '''
    # 迭代循环初始化参数
    for m in self.children():
        if isinstance(m, nn.Linear):
            nn.init.constant_(m.weight, 1)
            nn.init.constant_(m.bias, -100)
        # 也可以判断是否为conv2d，使用相应的初始化方式 
        elif isinstance(m, nn.Conv2d):
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

        elif isinstance(m, nn.BatchNorm2d):
            nn.init.constant_(m.weight.item(), 1)
            nn.init.constant_(m.bias.item(), 0)   
    '''


if __name__ == '__main__':
    qnet = DQNNet()
    x = torch.Tensor((2, 3))
    output = qnet.forward(x)
    print(output)