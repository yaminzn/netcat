from lib.models.cat_parts.tails.fluffy.const import FLUFFY_SVG
from lib.models.cat_parts.tails.tail import Tail
from lib.models.cat_parts.tails.const import TAIL


class Fluffy(Tail):
  name = TAIL.FLUFFY

  @property
  def svg(self):
    return FLUFFY_SVG.format(color=self.base_color)
