from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.asif.asif import Asif
from lib.models.cat_parts.eye_shapes.alien.alien import Alien
from lib.models.cat_parts.eye_shapes.stunned.stunned import Stunned
from lib.models.cat_parts.eye_shapes.slyboots.slyboots import Slyboots
from lib.models.cat_parts.eye_shapes.simple.simple import Simple


class CatEyeShapeFactory:
  @staticmethod
  def create(eye_shape_name: str):
    map = {
        EYE_SHAPE.ALIEN: Alien,
        EYE_SHAPE.ASIF: Asif,
        EYE_SHAPE.SIMPLE: Simple,
        EYE_SHAPE.SLYBOOTS: Slyboots,
        EYE_SHAPE.STUNNED: Stunned,
    }

    if eye_shape_name not in map:
      raise ValueError('Undefined eye shape: "{}"'.format(eye_shape_name))

    return map[eye_shape_name]
