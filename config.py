"""EasySaxo Alpha Main configuration"""

import sys

class App:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        self.dev = "SXF"
        self.problem = "in the chair"
        
easysaxo = App("EasySaxo", "Alpha 1.02") # yes im that lazy to write this ever again

COMMAND_REGISTRY = {}
GET_REGISTRY = {}
HELP_REGISTRY = {}

def register_command(name, aliases=None, help_text=None, registry=COMMAND_REGISTRY):
    def decorator(func):
        registry[name] = func
        HELP_REGISTRY[name] = help_text or func.__doc__ or "No usage details provided."
        if aliases:
            for alias in aliases:
                registry[alias] = func
                HELP_REGISTRY[alias] = HELP_REGISTRY[name]
        return func
    return decorator

# its ugly to be the 29th codeline in a config script. att, a pyzon comment 