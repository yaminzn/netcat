from lib.models.cat_parts.body.flame import FlameBody
from lib.models.cat_parts.body.grassy import GrassyBody


class CatBodyFactory:
  @staticmethod
  def create(body_name: str):
    map = {
        'flame': FlameBody,
        'grassy': GrassyBody,
    }

    if body_name not in map:
      raise ValueError('Undefined body: "{}"'.format(body_name))

    return map[body_name]
