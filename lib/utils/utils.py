from typing import List

import secrets


class Utils:
  @staticmethod
  def get_list_random_element(arr: List):
    return secrets.choice(arr)
