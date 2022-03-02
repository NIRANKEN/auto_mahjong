# -*- coding: utf-8 -*-
"""
UnitTest for component_detector
"""
import unittest
from recording_app.component_detector import detect_component, detect_component_type


class TestComponentDetector(unittest.TestCase):
  """
  UnitTest for component_detector.detect_component
  """

  def test_detect_component_success(self):
    self.assertEqual(detect_component("MAN1"), "MAN1")
    self.assertEqual(detect_component("PIN9"), "PIN9")
    self.assertEqual(detect_component("SOU5"), "SOU5")
    self.assertEqual(detect_component("CHUN"), "CHUN")
    self.assertEqual(detect_component("OK"), "OK")
    self.assertEqual(detect_component("REACH"), "REACH")

  def test_detect_component_error(self):
    with self.assertRaises(ValueError):
      detect_component("ERROR")

  def test_detect_component_type_success(self):
    self.assertEqual(detect_component_type("MAN1"), "MahjongTiles")
    self.assertEqual(detect_component_type("REACH"), "MahjongOperations")
    self.assertEqual(detect_component_type("OK"), "SystemOperations")

  def test_detect_component_type_error(self):
    with self.assertRaises(ValueError):
      detect_component_type("ERROR")


if __name__ == "__main__":
  unittest.main()
