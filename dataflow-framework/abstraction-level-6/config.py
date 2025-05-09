

CONFIG = {
    'start': 'processors.start.TagLines',  # Start node processor
    'error': 'processors.filters.OnlyError',  # Filter for error lines
    'warn': 'processors.filters.OnlyWarn',  # Filter for warn lines
    'general': 'processors.formatters.SnakeCase',  # Formatter for general lines
    'end': 'processors.output.Terminal'  # Output processor for termination
}
