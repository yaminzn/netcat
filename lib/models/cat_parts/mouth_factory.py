from lib.models.cat_parts.mouths.cheeky.cheeky import Cheeky
from lib.models.cat_parts.mouths.belch.belch import Belch
from lib.models.cat_parts.mouths.wuvme.wuvme import Wuvme
from lib.models.cat_parts.mouths.const import MOUTH
from lib.models.cat_parts.mouths.confuzzled.confuzzled import Confuzzled
from lib.models.cat_parts.mouths.yokel.yokel import Yokel


class CatMouthFactory:
  @staticmethod
  def create(mouth_name: str):
    map = {
        MOUTH.BELCH: Belch,
        MOUTH.CHEEKY: Cheeky,
        MOUTH.CONFUZZLED: Confuzzled,
        MOUTH.WUVME: Wuvme,
        MOUTH.YOKEL: Yokel,
    }

    if mouth_name not in map:
      raise ValueError('Undefined mouth name: "{}"'.format(mouth_name))

    return map[mouth_name]
