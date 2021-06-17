from lib.models.cat_parts.tails.const import TAIL
from lib.utils.utils import Utils
from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.mouths.const import MOUTH


class CatUtils:
  @staticmethod
  def get_random_body_name():
    return Utils.get_list_random_element([
        'flame',
        'grassy',
    ])

  @staticmethod
  def get_random_eye_shape_name():
    return Utils.get_list_random_element([
        EYE_SHAPE.ALIEN,
        EYE_SHAPE.ASIF,
        EYE_SHAPE.SIMPLE,
        EYE_SHAPE.SLYBOOTS,
        EYE_SHAPE.STUNNED,
    ])

  @staticmethod
  def get_random_mouth_name():
    return Utils.get_list_random_element([
        MOUTH.BELCH,
        MOUTH.CHEEKY,
        MOUTH.CONFUZZLED,
        MOUTH.WUVME,
        MOUTH.YOKEL,
    ])

  @staticmethod
  def get_random_tail_name():
    return Utils.get_list_random_element([
        TAIL.FLUFFY,
        TAIL.NORMAL,
        TAIL.SQUIRREL,
    ])
