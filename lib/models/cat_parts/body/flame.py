from lib.const.cat.body.flame import flame_svg


class FlameBody:
  name = 'flame'

  def __init__(self, base_color: str, accent_color: str) -> None:
    self.base_color = base_color
    self.accent_color = accent_color

  def get_svg(self):
    return flame_svg.format(
      base_color=self.base_color,
      accent_color=self.accent_color,
    )
