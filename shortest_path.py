class ShortestPath:
    def __init__(self, world):
        self.world = world
    def raw_distance(self, source, destination):
        result = {}
        for i in self.world[source]:
            for j in self.world[destination]:
                result[(i,j)] = abs(j - i)
        return result
    def distance_to_cost(self):
        houses_to_bridges = self.raw_distance("houses", "bridges")
        houses_to_ports = self.raw_distance("houses", "ports")
        for edge in houses_to_ports:
            houses_to_ports[edge] *= 2
        bridges_to_shops = self.raw_distance("bridges", "shops")
        ports_to_shops = self.raw_distance("ports", "shops")
        for edge in ports_to_shops:
            ports_to_shops[edge] *= 2
        return {
            "houses_to_bridges": houses_to_bridges,
            "houses_to_ports": houses_to_ports,
            "bridges_to_shops": bridges_to_shops,
            "ports_to_shops": ports_to_shops
        }
    def transitive_cost(self, costs, checkpoint1, checkpoint2):
        result = {}
        for i in costs[checkpoint1]:
            for j in costs[checkpoint2]:
                if i[1] == j[0]:
                    total_cost = costs[checkpoint1][i] + costs[checkpoint2][j] + 4
                    if (i[0], j[1]) not in result:
                        result[(i[0], j[1])] = total_cost
                    else:
                        if result[(i[0], j[1])] > total_cost:
                            result[(i[0], j[1])] = total_cost
        return result
    def find_all(self):
        point2point_cost = self.distance_to_cost()
        bike = self.transitive_cost(point2point_cost, "houses_to_bridges", "bridges_to_shops")
        boat = self.transitive_cost(point2point_cost, "houses_to_ports", "ports_to_shops")
        pairs = [(i, j) for i in self.world["houses"] for j in self.world["shops"]]
        costs = {}
        for pair in pairs:
            cost = None
            if bike[pair] > boat[pair]:
                cost = boat[pair]
            else:
                cost = bike[pair]
            costs[pair] = cost
        return costs



