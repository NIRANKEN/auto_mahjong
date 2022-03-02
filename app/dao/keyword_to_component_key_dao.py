# -*- coding: utf-8 -*-
"""
keyword_to_component_keyカラムに関するDB操作を定義します
"""
from typing import List
from dao.pymongo_client import get_database
from dao.dto.keyword_to_component_key_dto import KeywordToComponentKeywordDto

_col = "keyword_to_component_key"
_collection_name = get_database()[_col]


def insert(dto_list: List[KeywordToComponentKeywordDto]) -> None:
  """
  keyword_to_component_keyへのinsert操作を定義します
  """
  print(F"insert {dto_list} to {_col}")
  _collection_name.insert_many(dto_list)
  print(F"completed to insert to {_col}")


def select_all_keys() -> List[str]:
  key_list = []
  for item in _collection_name.find():
    key_list.append(str(item["_id"]))
  return key_list


def select_all() -> List[dict]:
  return _collection_name.find()
