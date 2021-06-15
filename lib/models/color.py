from lib.utils.color import ColorUtils


class Color:
  def __init__(self, hex_value: str) -> None:
      self.hex = hex_value

class NamedColor(Color):
  def __init__(self, color_name: str) -> None:
    hex_value = ColorUtils.get_named_color_hex_value(color_name);
    self.name = color_name
    super().__init__(hex_value)
