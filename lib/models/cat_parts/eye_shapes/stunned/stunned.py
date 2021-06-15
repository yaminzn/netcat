
from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.stunned.const import STUNNED_SVG
from lib.models.cat_parts.eye_shapes.eye_shape import EyeShape


class Stunned(EyeShape):
  name = EYE_SHAPE.STUNNED

  @property
  def svg(self):
    return STUNNED_SVG.format(eye_color=self.eye_color)
