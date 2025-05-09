# Configuration file for tag-to-processor mappings
PROCESSORS = {
    "start": "processors.start.tag_lines",
    "error": "processors.filters.only_error",
    "warn": "processors.filters.only_warn",
    "general": "processors.formatters.snakecase",
    "end": "processors.output.terminal"
}
