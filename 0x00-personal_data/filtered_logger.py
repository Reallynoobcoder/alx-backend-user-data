#!/usr/bin/env python3
"""A function filter_datum that returns the log message obfuscated."""
from typing import List, Tuple
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return an obfuscated log message."""
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
