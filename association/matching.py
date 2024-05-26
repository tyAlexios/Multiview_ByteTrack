import numpy as np
import torch
import lap

from scipy.optimize import linear_sum_assignment
from torchvision.transforms import transforms

transform = transforms.Compose(
    [transforms.ToTensor(), 
     transforms.Resize((320,320))]
)

@torch.no_grad()
def get_costs(encoder, imgs_a, imgs_b, device):
    inputs_a = torch.ones(1,3,320,320)
    inputs_b = torch.ones(1,3,320,320)
    
    for img_a, img_b in zip(imgs_a, imgs_b):
        img_a = transform(img_a).unsqueeze(0)
        img_b = transform(img_b).unsqueeze(0)
        
        inputs_a = torch.cat((inputs_a, img_a), dim=0)
        inputs_b = torch.cat((inputs_b, img_b), dim=0)
    
    inputs_a = inputs_a[1:].to(device)
    inputs_b = inputs_b[1:].to(device)
    
    feats_a = encoder(inputs_a)
    feats_b = encoder(inputs_b)
    
    M = feats_a.size(0)
    N = feats_b.size(0)
    
    distmat = torch.pow(feats_a, 2).sum(dim=1, keepdim=True).expand(M, N) + \
              torch.pow(feats_b, 2).sum(dim=1, keepdim=True).expand(N, M).t()
    distmat.addmm_(1, -2, feats_a, feats_b.t())
    
    return distmat.detach().cpu().numpy()

def linear_assignment(encoder, imgs_a, imgs_b, ids_a, ids_b, device):
    
    cost_matrix = get_costs(encoder, imgs_a, imgs_b, device)
    
    if cost_matrix.size == 0:
        return np.empty((0, 2), dtype=int), tuple(range(cost_matrix.shape[0])), tuple(range(cost_matrix.shape[1]))

    matches, unmatched_a, unmatched_b = [], [], []
    cost, x, y = lap.lapjv(cost_matrix, extend_cost=True, cost_limit=700.0)
    
    for ix, mx in enumerate(x):
        if mx >= 0:
            ids_b[mx] = ids_a[ix]

    return ids_b, unmatched_a, unmatched_b

