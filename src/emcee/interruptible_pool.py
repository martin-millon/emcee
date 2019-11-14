# -*- coding: utf-8 -*-

# The standard library now has an interruptible pool
from multiprocess.pool import Pool as InterruptiblePool

__all__ = ["InterruptiblePool"]
