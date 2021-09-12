class NodePriority(object):
    def __init__(self, name, index, parent,h_value):
        self.h_value = h_value
        self.name = name
        self.index = index
        self.parent = parent
        return

    def __lt__(self, other):
        return self.h_value < other.h_value