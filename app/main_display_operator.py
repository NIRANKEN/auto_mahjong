# -*- coding: utf-8 -*-
"""
9索にマウスカーソルもってく
"""
import pyautogui
import logging
from constants.consts import get_resource_image


def move_mouse_cursor(component_name: str, for_debug: bool = False) -> bool:
  result = None
  for position in pyautogui.locateAllOnScreen(
          get_resource_image(component_name), confidence=0.95):
    print(position)
    result = position
    pyautogui.moveTo(position, logScreenshot=for_debug)
    # 条件に当てはまるpositionを選ぶ。
  if result:
    logging.debug(result)
    return True
  else:
    logging.warning("コンポーネント:%s が見つかりませんでした", component_name)
    if for_debug:
      pyautogui.alert("This is the message to main display!")
    return False


if __name__ == "__main__":
  while True:
    if move_mouse_cursor("SOU9", for_debug=True):
      pyautogui.click()
