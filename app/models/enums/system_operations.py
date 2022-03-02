# -*- coding: utf-8 -*-
"""
麻雀(じゃんたま想定)操作をするためのComponent定義
"""
from enum import Enum, auto


class SystemOperations(Enum):
  """
  OK, キャンセルなどの基本操作のEnum
  """
  OK = auto()
  CANCEL = auto()
  CLICK = auto()
  SKIP = auto()
