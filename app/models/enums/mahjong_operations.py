# -*- coding: utf-8 -*-
"""
麻雀(じゃんたま想定)操作をするためのComponent定義
"""
from enum import Enum, auto


class MahjongOperations(Enum):
  """
  麻雀操作のEnum
  """
  PON = auto()
  KAN = auto()
  CHEE = auto()
  REACH = auto()
  RON = auto()
  TSUMO = auto()
