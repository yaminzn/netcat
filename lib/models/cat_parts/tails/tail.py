class Tail:
  _wrapper_svg_template = '''
    <g clip-path="url(#kittyClipPath)">
      {content}
    </g>
    '''
    
  svg: str = None

  def __init__(self, base_color: str) -> None:
    self.base_color = base_color

  def get_svg(self):
    return self._wrapper_svg_template.format(content=self.svg)
