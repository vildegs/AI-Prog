
class Node:
    g = 0
    h = 0
    parent = None
    domains = {}

    def __init__(self, parent, domains):
        self.parent = parent
        self.domains = domains
