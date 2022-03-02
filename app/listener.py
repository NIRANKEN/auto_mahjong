# -*- coding: utf-8 -*-
"""
麻雀牌・麻雀操作DB情報をもとに、発生した音声から麻雀牌・麻雀操作コンポーネントをクリックします
※resourcesに操作対象になる画像を入れて利用します
"""
import pyautogui
import logging
import sys

from component_detector import detect_component
from recognizer.google_speech_recognizer import get_speaking_value
import dao.keyword_to_component_key_dao as keyword_dao
from main_display_operator import move_mouse_cursor


logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler("listener.log"),
    logging.StreamHandler(sys.stdout)
])


def _create_keyword_to_component_dict() -> dict:
  """
  DBから、{音声認証テキストKey: 麻雀操作コンポーネントKey}のリストを取得し、
  音声認証テキストKey -> 麻雀操作コンポーネントKeyの辞書を作成します
  """
  keywords_from_db = keyword_dao.select_all()
  keyword_to_component = dict()
  for keyword_dto in keywords_from_db:
    dict_key = keyword_dto["_id"]
    dict_val = keyword_dto[dict_key]
    logging.info(
        "keyword_dto_from_db: "
        "{{dict_key: %s, dict_val: %s}}", dict_key, dict_val)
    keyword_to_component[dict_key] = dict_val
  return keyword_to_component


if __name__ == "__main__":
  keyword_to_compnent_dict = _create_keyword_to_component_dict()
  while True:
    speaking_result = get_speaking_value(is_notify=True)
    try:
      component_key = detect_component(
          keyword_to_compnent_dict[speaking_result])
    except KeyError:
      logging.warning("入力音声(%s)が、麻雀操作に変換できませんでした", speaking_result)
      continue
    print(component_key)
    if move_mouse_cursor(component_key):
      # pyautogui.alert("ここでくりっく")
      pyautogui.click()
      # pyautogui.doubleClick()
