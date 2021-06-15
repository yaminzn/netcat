class Mouth:
  _wrapper_svg_template = '''
    <g id="mouth">
      {content}
    </g>
    '''
    
  svg: str = None

  def get_svg(self):
    return self._wrapper_svg_template.format(content=self.svg)
