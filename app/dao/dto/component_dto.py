# -*- coding: utf-8 -*-
"""
mongoDBのcomponentのカラムに関するDB操作を定義します
"""
from typing import NewType
from component_detector import detect_component_type

ComponentDto = NewType("ComponentDto", dict)


def get_json_string(component_key: str, keyword_list: str) -> ComponentDto:
  """
  { keyword(音声認識結果のテキスト): component_key }のJSONを作成します。
  """
  dto = dict()
  dto["_id"] = component_key
  component_info = dict()
  component_info["component_type"] = detect_component_type(component_key)
  component_info["keyword"] = keyword_list
  dto[component_key] = component_info
  return ComponentDto(dto)
