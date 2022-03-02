# -*- coding: utf-8 -*-
"""
麻雀操作ComponentのEnumを返却します
"""

from models.enums.mahjong_tiles import MahjongTiles
from models.enums.mahjong_operations import MahjongOperations
from models.enums.system_operations import SystemOperations


def detect_component(component_name: str) -> str:
  """
  component_nameが、麻雀操作Component(麻雀牌、麻雀操作、基本操作)に属する場合、
  その名前を返却し、そうでなければValueErrorを返します。
  """
  if component_name:
    for tile in MahjongTiles:
      if tile.name == component_name:
        return tile.name
    for operation in MahjongOperations:
      if operation.name == component_name:
        return operation.name
    for operation in SystemOperations:
      if operation.name == component_name:
        return operation.name
  raise ValueError("invalid argument value: " + component_name)


def detect_component_type(component_name: str) -> str:
  """
  component_nameが、麻雀操作Component(麻雀牌、麻雀操作、基本操作)に属する場合、
  その名前を返却し、そうでなければValueErrorを返します。
  """
  if component_name:
    for tile in MahjongTiles:
      if tile.name == component_name:
        return "MahjongTiles"
    for operation in MahjongOperations:
      if operation.name == component_name:
        return "MahjongOperations"
    for operation in SystemOperations:
      if operation.name == component_name:
        return "SystemOperations"
  raise ValueError("invalid argument component type: " + component_name)
