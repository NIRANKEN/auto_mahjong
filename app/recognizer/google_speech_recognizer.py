# -*- coding: utf-8 -*-
"""
Google Speech Recognitionを利用して、発声した音声を文字認証して変換します
"""
import speech_recognition as sr
import logging
import simpleaudio
from constants.consts import get_resource_wav
# import subprocess
# import pyaudio


def get_speaking_value(is_notify=False) -> str:
  """
  音声入力から、Google Speech Recognizerで認証した結果文字列を返却します
  """

  r = sr.Recognizer()
  # py_audio = pyaudio.PyAudio()
  # print(F"device count:{py_audio.get_device_count()}")
  # print(py_audio.get_device_info_by_index(0))
  # print(py_audio.get_device_info_by_index(1))
  # print(",".join(sr.Microphone.list_microphone_names()))

  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    if is_notify:
      simpleaudio.WaveObject.from_wave_file(
          get_resource_wav("SpeechOn")).play().wait_done()
    logging.info("=== 何か、話しかけてください ===")
    audio = r.listen(source)
    logging.info("[o] ===> オーディオGET")

    try:
      logging.info("=== Google Speech Recognition(GSR)音声解析中 ===")
      keyword = r.recognize_google(audio, language="ja-JP")
      logging.info("You said : %s", keyword)
      return keyword
    except sr.UnknownValueError:
      logging.warning("Google Speech Recognition(GSR)は音声を認識できませんでした")
      pass
    except sr.RequestError as e:
      logging.error("GSR Request Error; %s", e)
      logging.error("ネットワークに接続できているか確認してください")
      pass


if __name__ == "__main__":
  result = get_speaking_value()
  if result:
    print("result: " + result)
