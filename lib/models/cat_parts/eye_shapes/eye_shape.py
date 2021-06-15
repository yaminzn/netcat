class EyeShape:
  _wrapper_svg_template = '''
    <g id="eye">
      {content}
    </g>
    '''
  svg: str = None

  def __init__(self, eye_color: str) -> None:
    self.eye_color = eye_color

  def get_svg(self):
    return self._wrapper_svg_template.format(content=self.svg)
