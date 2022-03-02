# -*- coding: utf-8 -*-
"""
麻雀牌・麻雀操作を認識するDBつくる処理
"""
import argparse
import logging
import sys
from component_detector import detect_component
from recognizer.google_speech_recognizer import get_speaking_value
from utils.yes_no_input_util import yes_no_input
import dao.keyword_to_component_key_dao as keyword_dao
from dao.dto.keyword_to_component_key_dto import get_json_string as get_keyword_json

logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler("recorder.log"),
    logging.StreamHandler(sys.stdout)
])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input",
                      help="録音対象の麻雀操作Componentキーを設定します")
  args = parser.parse_args()
  component_key = detect_component(args.input)

  keyword_from_db = keyword_dao.select_all_keys()
  logging.debug("keyword_from_db: %s", keyword_from_db)
  keyword_list = []
  keyword_dto_list = []
  for idx in range(5):
    speaking_result = get_speaking_value(is_notify=True)
    if speaking_result in keyword_list \
            or speaking_result in keyword_from_db or speaking_result is None:
      logging.debug("処理をスキップします")
      continue
    print(F"{speaking_result}を新しい単語として登録しますか？")
    if yes_no_input():
      logging.info("%sは新しい単語のため、登録処理の準備をします", speaking_result)
      keyword_list.append(speaking_result)
      keyword_dto_list.append(get_keyword_json(speaking_result, component_key))
    else:
      logging.info("%sの登録を見送ります", speaking_result)
      continue
  if keyword_dto_list:
    logging.info("%s個の単語をKeywordに登録します", len(keyword_dto_list))
    keyword_dao.insert(keyword_dto_list)
  logging.info("%sの登録処理が完了しました", component_key)
