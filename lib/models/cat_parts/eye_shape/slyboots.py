from lib.const.cat.eye_shape.slyboots import slyboots_svg


class SlybootsEyeShape:
  name = 'slyboots'
  
  def __init__(self, eye_color: str) -> None:
    self.eye_color = eye_color

  def get_svg(self):
    return slyboots_svg.format(eye_color=self.eye_color)
