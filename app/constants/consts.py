
import logging

_PROJECT_ROOT = "D:/Programs/auto_mahjong"


def get_project_root() -> str:
  return _PROJECT_ROOT


def get_resource_image(component_name: str) -> str:
  r_path = F"{_PROJECT_ROOT}/resources/{component_name}.png"
  logging.debug("%s のリソースを画像認識に利用します", r_path)
  return r_path


def get_resource_wav(wav_name: str) -> str:
  r_path = F"{_PROJECT_ROOT}/resources/{wav_name}.wav"
  logging.debug("%s のwavを利用します", r_path)
  return r_path
