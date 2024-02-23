#!/usr/bin/env python
import sys
import os.path as osp
cur_dir = osp.dirname(__file__)
sys.path.insert(0, osp.join(cur_dir, '../'))

from greenthread.monkey import monkey_patch; monkey_patch()
from greenthread.green import *

GreenTimeout(0.1)
green_sleep(0.2)
