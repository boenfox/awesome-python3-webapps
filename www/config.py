#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#config.py

import config_default

configs = config_default.configs
try:
    import config_overide
    config = merge(configs, config_overide.configs)
except ImportError:
    pass