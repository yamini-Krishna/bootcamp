from collections import defaultdict

def run_dag(config, start_node, input_lines):
    processors = config["processors"]
    graph = config["graph"]

    state = defaultdict(list)
    state[start_node] = input_lines

    queue = [start_node]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)

        processor = processors[node]
        input_data = state[node]

        if not input_data:
            continue

        results = processor(input_data)

        for tag, line in results:
            for child in graph.get(node, []):
                state[child].append((tag, line))
                if child not in visited:
                    queue.append(child)
