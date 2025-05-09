from processors import (
    trim_processor,
    tag_error_processor,
    tag_warn_processor,
    archive_processor,
    count_processor,
    print_processor
)

CONFIG = {
    "processors": {
        "trim": trim_processor(),
        "tag_error": tag_error_processor(),
        "tag_warn": tag_warn_processor(),
        "archive": archive_processor(),
        "count": count_processor(),
        "print": print_processor()
    },
    "graph": {
        "trim": ["tag_error", "tag_warn"],
        "tag_error": ["archive", "count"],
        "tag_warn": ["print"],
        "archive": [],
        "count": [],
        "print": []
    }
}
