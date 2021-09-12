class NodePriority(object):
    def __init__(self, node_name, h_value):
        self.h_value = h_value
        self.node_name = node_name
        #return

    def __lt__(self, other):
        return self.h_value < other.h_value