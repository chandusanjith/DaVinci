from django.shortcuts import render
from googletrans import Translator


def _translate(response_to_be_converted, language):
  print(type(response_to_be_converted))
  out_context = {}
  for key, value in response_to_be_converted.items():
    print(key)
    print(value)
    translator = Translator()
    result = translator.translate(value, dest=language).text
    out_context[key] = result
    print(result)
  return out_context
  