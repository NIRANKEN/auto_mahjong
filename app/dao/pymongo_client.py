# -*- coding: utf-8 -*-
"""
麻雀DB Clientの取得
"""
from pymongo import MongoClient
import certifi
import os


def get_database() -> MongoClient:
  """
  麻雀DBの取得をします
  """
  ca = certifi.where()
  client = MongoClient(_get_connection_url(), tlsCAFile=ca)

  return client["mahjong"]


def _get_connection_url():
  db_user = os.environ["MAHJONG_DB_USER"]
  db_pass = os.environ["MAHJONG_DB_PASS"]
  db_cluster = os.environ["MAHJONG_DB_CLUSTER"]
  return "mongodb+srv://" \
      + db_user + ":" + db_pass \
      + "@" + db_cluster + ".mongodb.net/myFirstDatabase"


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

  # Get the database
  dbname = get_database()
  print(dbname.list_collection_names())
