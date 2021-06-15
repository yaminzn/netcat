from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.asif.const import ASIF_SVG
from lib.models.cat_parts.eye_shapes.eye_shape import EyeShape


class Asif(EyeShape):
  name = EYE_SHAPE.ASIF

  @property
  def svg(self):
    return ASIF_SVG.format(eye_color=self.eye_color)
