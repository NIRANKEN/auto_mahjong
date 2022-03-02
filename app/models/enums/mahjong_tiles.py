# -*- coding: utf-8 -*-
"""
麻雀(じゃんたま想定)操作をするためのComponent定義
"""
from enum import Enum, auto


class MahjongTiles(Enum):
  """
  麻雀牌のEnum
  """
  MAN1 = auto()
  MAN2 = auto()
  MAN3 = auto()
  MAN4 = auto()
  MAN5 = auto()
  MAN6 = auto()
  MAN7 = auto()
  MAN8 = auto()
  MAN9 = auto()

  PIN1 = auto()
  PIN2 = auto()
  PIN3 = auto()
  PIN4 = auto()
  PIN5 = auto()
  PIN6 = auto()
  PIN7 = auto()
  PIN8 = auto()
  PIN9 = auto()

  SOU1 = auto()
  SOU2 = auto()
  SOU3 = auto()
  SOU4 = auto()
  SOU5 = auto()
  SOU6 = auto()
  SOU7 = auto()
  SOU8 = auto()
  SOU9 = auto()

  TON = auto()
  NAN = auto()
  SYA = auto()
  PEI = auto()

  HAKU = auto()
  HATSU = auto()
  CHUN = auto()

  MAN5RED = auto()
  PIN5RED = auto()
  SOU5RED = auto()
