from lib.const.color import Colors
import secrets


class ColorUtils:
  @staticmethod
  def get_random_color_name():
    return secrets.choice(list(Colors.keys()))

  @staticmethod
  def get_random_named_color_hex_value():
    random_key = ColorUtils.get_random_color_name()

    return Colors[random_key]

  @staticmethod
  def get_named_color_hex_value(color_name: str):
    if color_name not in Colors:
      raise ValueError('Undefined color: "{}"'.format(color_name))

    return Colors[color_name]
