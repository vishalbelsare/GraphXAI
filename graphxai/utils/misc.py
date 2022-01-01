import torch
from torch import Tensor
from torch.nn import PairwiseDistance as pdist


def make_node_ref(nodes: torch.Tensor):
    '''
    Makes a node reference to unite node indicies across explanations
    Args:
        nodes (torch.tensor): Tensor of nodes to reference.
    '''
    node_reference = {nodes[i].item():i for i in range(nodes.shape[0])}
    return node_reference

def node_mask_from_edge_mask(node_subset: torch.Tensor, edge_index: torch.Tensor, edge_mask: torch.Tensor):
    mask_eidx = edge_index[:,edge_mask]

    unique_nodes = torch.unique(mask_eidx)

    print('unique_nodes', unique_nodes)

    node_mask = torch.tensor([node_subset[i] in unique_nodes for i in range(node_subset.shape[0])])
    
    return node_mask.float()



def distance(emb_1: torch.tensor, emb_2: torch.tensor, p=2) -> float:
    '''
    Calculates the distance between embeddings generated by a GNN model
    Args:
        emb_1 (torch.tensor): embeddings for the clean graph
        emb_2 (torch.tensor): embeddings for the perturbed graph
    '''
    if p == 0:
        return torch.dist(emb_1, emb_2, p=0).item()
    elif p == 1:
        return torch.dist(emb_1, emb_2, p=1).item()
    elif p == 2:
        return torch.dist(emb_1, emb_2, p=2).item()
    else:
        print('Invalid choice! Exiting..')


# def make_edge_ref():
#     pass