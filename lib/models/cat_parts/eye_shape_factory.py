from lib.models.cat_parts.eye_shape.simple import SimpleEyeShape
from lib.models.cat_parts.eye_shape.slyboots import SlybootsEyeShape
from lib.models.cat_parts.eye_shape.stunned import StunnedEyeShape


class CatEyeShapeFactory:
  @staticmethod
  def create(eye_shape_name: str):
    map = {
        'simple': SimpleEyeShape,
        'slyboots': SlybootsEyeShape,
        'stunned': StunnedEyeShape,
    }

    if eye_shape_name not in map:
      raise ValueError('Undefined eye shape: "{}"'.format(eye_shape_name))

    return map[eye_shape_name]
