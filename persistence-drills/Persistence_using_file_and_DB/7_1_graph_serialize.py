import json

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes  # e.g., ['A', 'B', 'C']
        self.edges = edges  # e.g., [('A', 'B'), ('B', 'C')]

    def to_json(self):
        graph_data = {
            'nodes': self.nodes,
            'edges': self.edges
        }
        return json.dumps(graph_data)

# Example usage
graph = Graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'C')])
json_data = graph.to_json()
print(json_data)
