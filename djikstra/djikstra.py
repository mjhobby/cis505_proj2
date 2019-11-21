class Edge(object):
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def __str__(self):
        return "{}-{}->{}".format(self.start, self.cost, self.end)


class Node(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

