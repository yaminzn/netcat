from lib.const.cat.eye_shape.stunned import stunned_svg


class StunnedEyeShape:
  name = 'stunned'
  
  def __init__(self, eye_color: str) -> None:
    self.eye_color = eye_color

  def get_svg(self):
    return stunned_svg.format(eye_color=self.eye_color)
