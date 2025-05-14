import json

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data['nodes'], data['edges'])

# Example JSON string
json_string = '{"nodes": ["A", "B", "C"], "edges": [["A", "B"], ["B", "C"]]}'

graph = Graph.from_json(json_string)
print(graph.nodes)
print(graph.edges)
