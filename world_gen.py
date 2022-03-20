class GenerateWorld:
    def __init__(self):
        pass
    def get_data(self, context):
        n = int(input(f"\nnumber of {context}s: "))
        result = []
        for i in range(n):
            result.append(int(input(f"{context} {i+1} of {n}: ")))
        return result
    def aggregate_input(self):
        houses = self.get_data("house")
        shops = self.get_data("shop")
        bridges = self.get_data("bridge")
        ports = self.get_data("port")
        return {
            "houses": houses,
            "shops": shops,
            "bridges": bridges,
            "ports": ports, 
        }