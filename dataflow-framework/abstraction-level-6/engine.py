# engine.py

import networkx as nx
from importlib import import_module
from typing import Iterator, Tuple

def run_dag(config: dict, start_tag: str, input_lines: Iterator[str]) -> None:
    """
    Runs the state-based routing system based on the configuration.
    :param config: Mapping of tags to processor modules
    :param start_tag: The initial tag to start processing
    :param input_lines: Input lines that will be processed
    """
    # Create a directed graph to represent the routing system
    graph = nx.DiGraph()

    # Register processors from config
    for tag, processor in config.items():
        module_name, class_name = processor.rsplit('.', 1)
        module = import_module(module_name)
        processor_class = getattr(module, class_name)
        graph.add_node(tag, processor=processor_class())

    # Setup the start processor
    current_tags = [start_tag]

    while current_tags:
        tag = current_tags.pop(0)  # Process the next tag

        # Get the processor for this tag
        processor = graph.nodes[tag]['processor']

        # Process the lines
        lines = processor.process(input_lines)

        for next_tag, line in lines:
            if next_tag == 'end':
                print(f"End reached with line: {line}")
                return
            if next_tag in graph:
                current_tags.append(next_tag)
            else:
                print(f"Invalid tag encountered: {next_tag}")
                return
