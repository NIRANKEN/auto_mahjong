# -*- coding: utf-8 -*-
"""
mongoDBのkeyword_to_component_keyのカラムに関するDB操作を定義します
"""

from typing import NewType


KeywordToComponentKeywordDto = NewType("KeywordToComponentKeywordDto", dict)


def get_json_string(keyword: str, component_key: str) -> KeywordToComponentKeywordDto:
  """
  { keyword(音声認識結果のテキスト): component_key }のJSONを作成します。
  """
  dto = dict()
  dto["_id"] = keyword
  dto[keyword] = component_key
  return KeywordToComponentKeywordDto(dto)
