from lib.models.cat_parts.eye_shape_factory import CatEyeShapeFactory
from lib.utils.cat import CatUtils
from lib.models.cat_parts.body_factory import CatBodyFactory
from lib.models.color import NamedColor
from lib.utils.color import ColorUtils


class Cat:
  svg_template = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3000 3000" xmlns:xlink="http://www.w3.org/1999/xlink">{content}</svg>'

  def __init__(
      self,
      body_name: str = None,
      eye_shape_name: str = None,
      mouth_name: str = None,
      eye_color_name: str = None,
      base_color_name: str = None,
      accent_color_name: str = None,
      highlight_color_name: str = None,
  ) -> None:
    self.eye_color = NamedColor(eye_color_name or ColorUtils.get_random_color_name())
    self.base_color = NamedColor(base_color_name or ColorUtils.get_random_color_name())
    self.accent_color = NamedColor(accent_color_name or ColorUtils.get_random_color_name())
    self.highlight_color = NamedColor(highlight_color_name or ColorUtils.get_random_color_name())

    print('baseColor', self.base_color)
    print('accentColor', self.accent_color)
    print('highlightColor', self.highlight_color)

    BodyClass = CatBodyFactory.create(body_name or CatUtils.get_random_body_name())
    print('BodyClass', BodyClass)
    self.body = BodyClass(self.base_color.hex, self.accent_color.hex)
    print('body', self.body)
    print('highlightColor', self.highlight_color)

    EyeShapeClass = CatEyeShapeFactory.create(eye_shape_name or CatUtils.get_random_eye_shape_name())
    print('EyeShapeClass', EyeShapeClass)
    self.eye_shape = EyeShapeClass(self.eye_color.hex)
    print('eye_shape', self.eye_shape)

  def get_svg(self):
    body_svg = self.body.get_svg()
    eye_shape_svg = self.eye_shape.get_svg()

    return self.svg_template.format(content=body_svg+eye_shape_svg)
