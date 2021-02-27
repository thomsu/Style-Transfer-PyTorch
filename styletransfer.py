import torch
import torch.nn as nn
import torch.optim as optim
from PIL import Image
import torchvision.transform as transform
import torchvision.models as models
from torchvision.utils import save_image


class VGG(nn.Module):
    def __init__(self):
        super(VGG, self).__init__():

        self.chosen_features = [0, 5, 10, 19, 28]
        self.model = models.vgg19(pretrained=True).features[:29]

    def forward(self, x):
        features = []

        for layer_num, layer in enumerate(self.model):
            x = layer(x)

            if layer_num in self.chosen_features:
                features.append(x)

        return features
