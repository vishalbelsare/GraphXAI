import random
import torch

from graphxai.explainers import RandomExplainer
from graphxai.explainers.utils.visualizations import visualize_subgraph_explanation
from graphxai.gnn_models.node_classification import BA_Houses, GCN, train, test


n = 300
m = 2
num_houses = 20

bah = BA_Houses(n, m)
data, inhouse = bah.get_data(num_houses)

model = GCN(64, input_feat = 1, classes = 2)
print(model)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
criterion = torch.nn.CrossEntropyLoss()

for epoch in range(1, 201):
    loss = train(model, optimizer, criterion, data)
    acc = test(model, data)
    print(f'Epoch: {epoch:03d}, Loss: {loss:.4f}, Test Acc: {acc:.4f}')

node_idx = random.choice(inhouse)

model.eval()
pred = model(data.x, data.edge_index)[node_idx, :].reshape(-1, 1)
print('pred shape', pred.shape)
print('GROUND TRUTH LABEL: \t {}'.format(data.y[node_idx].item()))
print('PREDICTED LABEL   : \t {}'.format(pred.argmax(dim=0).item()))

act = lambda x: torch.argmax(x, dim=1)
explainer = RandomExplainer(model)

exp, khop_info = explainer.get_explanation_node(data.x, node_idx = int(node_idx), edge_index = data.edge_index)
