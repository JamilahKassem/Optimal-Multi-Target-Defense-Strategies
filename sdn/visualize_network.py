import pandas as pd
import numpy as np
import networkx as nx
from IPython.display import display, HTML
from pyvis.network import Network

def visualize_net(data,n):
    g = nx.Graph()

    # Add nodes
    for host in data.hosts:
        g.add_node(host.name, label=host.name, font={'size': 25}, shape='image', image='https://img.icons8.com/color/48/000000/laptop.png', size=25)
    for switch in data.switches:
        g.add_node(switch.name, label=switch.name, font={'size': 25}, shape='image', image='https://img.icons8.com/color/48/000000/switch.png', size=25)
    # Add links
    for link in data.links:
        n1 = link.intf1.node.name
        n2 = link.intf2.node.name
        if n1 == "s0" and n2 != "Main":
            g.add_edge(n1, n2,
                width=8,
                color='black',
                label=f"Path {int(n2[1:])}",
                dashes=False,
                smooth=True,
                font={'size': 25} )
        else:
            g.add_edge(n1, n2,
                width=8,
                color='black',
                dashes=False,
                smooth=True )

    net = Network(notebook=True)
    net.from_nx(g)

    net.save_graph("topology.html")

    # Modify the HTML file to include height:100%
    with open("topology.html", "r") as file:
        html = file.read()

    # Replace the div style
    html = html.replace(
        '<div class="card" style="width: 100%">',
        '<div class="card" style="width: 100%; height: 100%">'
    )

    # Save back
    with open("topology.html", "w") as file:
        file.write(html)