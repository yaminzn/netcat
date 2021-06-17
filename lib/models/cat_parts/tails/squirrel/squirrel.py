from lib.models.cat_parts.tails.squirrel.const import SQUIRREL_SVG
from lib.models.cat_parts.tails.tail import Tail
from lib.models.cat_parts.tails.const import TAIL


class Squirrel(Tail):
  name = TAIL.SQUIRREL

  @property
  def svg(self):
    return SQUIRREL_SVG.format(color=self.base_color)
