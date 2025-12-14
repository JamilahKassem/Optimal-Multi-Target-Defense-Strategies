import numpy as np

class ParentNode:
    def __init__(self):
        self.nodes = []
s
    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return f"MyObject(data={self.nodes})"

class ChildResource:
    def __init__(self):
        self.resources = []
        self.alphas = []

    def add_resource(self, resource, alpha):
        self.resources.append(resource)
        self.alphas.append(alpha)

    def __repr__(self):
        return f"MyObject(data={self.resources})"

def calculate_alpha(R, m, n):
    alpha = np.zeros((m, n))
    ParentNodes = []
    # initialize an array pointing to all the nodes that the resource moves between
    for i in range(m):
        ParentNodes.append(ParentNode())
    ChildResources = []
    for i in range(n):
        ChildResources.append(ChildResource())
    total_criticality = 0
    for criticality in R:
       total_criticality = total_criticality + criticality

    criticality_for_node = total_criticality / n # Calculate the criticality needed to be able to fill a node
    i = 0
    k = 0
    alpha_resource_remaining = np.ones(m) # alpha remaining fore resource
    while R[i] >= criticality_for_node: # set all resources that can fill node
        while alpha_resource_remaining[i] > criticality_for_node / R[i]:
            alpha[i, k] = criticality_for_node / R[i]
            ParentNodes[i].add_node(k)
            ChildResources[k].add_resource(i,alpha[i, k])
            alpha_resource_remaining[i] = alpha_resource_remaining[i] - alpha[i, k]
            k = k + 1
        i = i + 1
    i = 0
    i2 = m-1
    alpha_node_remaining = criticality_for_node # set remaining alpha
    while k < n and i2 > 0: # set remaining alpha
        if alpha_node_remaining < alpha_resource_remaining[i] * R[i] or alpha_resource_remaining[i] == 0: # use low resources in case high resources are not enough
            while i2 > 0 and alpha_node_remaining > alpha_resource_remaining[i2] * R[i2]:
                alpha[i2, k] = alpha_resource_remaining[i2]
                ParentNodes[i2].add_node(k)
                ChildResources[k].add_resource(i2,alpha[i2, k])
                alpha_node_remaining = alpha_node_remaining - alpha_resource_remaining[i2] * R[i2]
                i2 = i2 - 1
            if i2 > 0:
                alpha[i2, k] = alpha_node_remaining / R[i2]
                ParentNodes[i2].add_node(k)
                ChildResources[k].add_resource(i2,alpha[i2, k])
                alpha_resource_remaining[i2] = alpha_resource_remaining[i2] - alpha[i2, k]
                k = k + 1
                alpha_node_remaining = criticality_for_node
        else:
            alpha[i, k] = alpha_resource_remaining[i]
            ParentNodes[i].add_node(k)
            ChildResources[k].add_resource(i,alpha[i, k])
            alpha_node_remaining = alpha_node_remaining - alpha_resource_remaining[i] * R[i]
            alpha_resource_remaining[i] = 0
            i = i + 1
            if R[i] < criticality_for_node:
                i = i - 1

    return alpha, ParentNodes, ChildResources
