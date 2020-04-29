import json
import sys


class ConfigWrapper:
    def __init__(self, d=dict()):
        self.d = d

    def __getattr__(self, item):
        if item in self.d.keys():
            return self.d[item]
        else:
            return None


with open('bot_config.json') as cfg:
    sys.modules[__name__] = ConfigWrapper(json.load(cfg))
