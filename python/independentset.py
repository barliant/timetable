#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     16-03-2014
# Copyright:   (c) acer 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import networkx as nx

def main():
    ig = nx.Graph()
    ig.add_edge(1,2)
    ig.add_edge(1,3)
    ig.add_edge(2,3)
    ig.add_edge(2,4)
    ig.add_edge(2,5)
    ig.add_edge(3,6)
    ig.add_edge(3,7)
    ig.add_edge(4,7)
    ig.add_edge(5,7)
    ig.add_edge(6,7)
    for node in ig.nodes():
        print node, nx.node_connected_component(ig, node)

if __name__ == '__main__':
    main()
