from lib.models.cat_parts.tails.const import TAIL
from lib.models.cat_parts.tails.fluffy.fluffy import Fluffy
from lib.models.cat_parts.tails.normal.normal import Normal
from lib.models.cat_parts.tails.squirrel.squirrel import Squirrel


class CatTailFactory:
  @staticmethod
  def create(tail_name: str):
    map = {
        TAIL.FLUFFY: Fluffy,
        TAIL.NORMAL: Normal,
        TAIL.SQUIRREL: Squirrel,
    }

    if tail_name not in map:
      raise ValueError('Undefined tail: "{}"'.format(tail_name))

    return map[tail_name]
