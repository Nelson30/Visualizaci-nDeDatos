import igraph
import numpy as np
import pandas as pd
from network2tikz import plot

#data = pd.read_csv('')
#data.loc(:, "")

net = igraph.Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3),
                    (5,6), (6,6)],directed=True)

net.vs["name"] = ["Alajuela", "Heredia", "Cartago", "PZ", "Saprissa", "San Carlos", "Grecia"]
net.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
net.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
net.es["is_formal"] = [False, False, True, True, True, False, True, False,
                       False, False]

layout = {0: (4.3191, -3.5352), 1: (0.5292, -0.5292),
          2: (8.6559, -3.8008), 3: (12.4117, -7.5239),
          4: (12.7, -1.7069), 5: (6.0022, -9.0323),
          6: (9.7608, -12.7)}

color_dict = {'m': 'blue', 'f': 'red'}
visual_style = {}

visual_style['vertex_size'] = .5
visual_style['vertex_color'] = [color_dict[g] for g in net.vs['gender']]
visual_style['vertex_opacity'] = .7
visual_style['vertex_label'] = net.vs['name']
visual_style['vertex_label_position'] = 'below'

visual_style['edge_width'] = [1 + 2 * int(f) for f in net.es['is_formal']]
visual_style['edge_curved'] = 0.1

visual_style['layout'] = layout
visual_style['canvas'] = (8,8)
visual_style['margin'] = 1

plot(net,**visual_style)