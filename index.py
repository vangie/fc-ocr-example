# -*- coding: utf-8 -*-
import logging
from tesserocr import PyTessBaseAPI

def handler(event, context):
  api = PyTessBaseAPI()
  api.SetImageFile("sample.jpg")
  txt = api.GetUTF8Text()
  logging.info(txt)
  logging.info(api.AllWordConfidences())
  return txt