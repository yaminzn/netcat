from lib.models.cat_parts.tails.normal.const import NORMAL_SVG
from lib.models.cat_parts.tails.tail import Tail
from lib.models.cat_parts.tails.const import TAIL


class Normal(Tail):
  name = TAIL.NORMAL

  @property
  def svg(self):
    return NORMAL_SVG.format(color=self.base_color)
