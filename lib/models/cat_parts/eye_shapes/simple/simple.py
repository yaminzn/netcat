from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.simple.const import SIMPLE_SVG
from lib.models.cat_parts.eye_shapes.eye_shape import EyeShape


class Simple(EyeShape):
  name = EYE_SHAPE.SIMPLE

  @property
  def svg(self):
    return SIMPLE_SVG.format(eye_color=self.eye_color)
