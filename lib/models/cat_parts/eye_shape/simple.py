from lib.const.cat.eye_shape.simple import simple_svg


class SimpleEyeShape:
  name = 'simple'

  def __init__(self, eye_color: str) -> None:
    self.eye_color = eye_color

  def get_svg(self):
    return simple_svg.format(eye_color=self.eye_color)
