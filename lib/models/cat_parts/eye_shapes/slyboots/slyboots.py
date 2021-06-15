from lib.models.cat_parts.eye_shapes.const import EYE_SHAPE
from lib.models.cat_parts.eye_shapes.slyboots.const import SLYBOOTS_SVG
from lib.models.cat_parts.eye_shapes.eye_shape import EyeShape


class Slyboots(EyeShape):
  name = EYE_SHAPE.SLYBOOTS

  @property
  def svg(self):
    return SLYBOOTS_SVG.format(eye_color=self.eye_color)
