import torch.nn as nn


class Critic(nn.Module):
    # 得到V(s)
    def __init__(self, n_features):
        super(Critic, self).__init__()
        self.n_features = n_features
        self.n_output = 1

        self.layers = nn.Sequential(
            nn.Linear(self.n_features, self.n_features * 8),
            nn.PReLU(),
            nn.Linear(self.n_features * 8, self.n_features * 8),
            nn.PReLU(),
            nn.Linear(self.n_features * 8, self.n_output)
        )

    def forward(self, x):
        return self.layers(x)

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

