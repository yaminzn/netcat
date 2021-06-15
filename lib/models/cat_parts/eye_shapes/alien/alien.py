from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.alien.const import ALIEN_SVG
from lib.models.cat_parts.eye_shapes.eye_shape import EyeShape


class Alien(EyeShape):
  name = EYE_SHAPE.ALIEN

  @property
  def svg(self):
    return ALIEN_SVG.format(eye_color=self.eye_color)
