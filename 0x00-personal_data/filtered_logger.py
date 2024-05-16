#!/usr/bin/env python3
"""A function filter_datum that returns the log message obfuscated."""
from typing import List, Tuple
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Returns the log message obfuscated."""
    return re.sub(r'({})=[^{}{}]+'.format('|'.join(fields),
                                          re.escape(redaction),
                                          re.escape(separator)),
                  r'\1={}{}'.format(redaction,
                                    separator),
                  message)
