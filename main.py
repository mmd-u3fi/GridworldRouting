from shortest_path import ShortestPath
from world_gen import GenerateWorld

world = GenerateWorld()
coords = world.aggregate_input()

pathfinder = ShortestPath(coords)
pairs = pathfinder.find_all()
print('\n')
for pair in pairs:
    print(f"house {pair[0]} -> shop {pair[1]}: {pairs[pair]}")
