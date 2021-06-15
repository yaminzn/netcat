from lib.models.cat_parts.mouths.cheeky.const import CHEEKY_SVG
from lib.models.cat_parts.mouths.mouth import Mouth
from lib.models.cat_parts.mouths.const import MOUTH


class Cheeky(Mouth):
  _wrapper_svg_template = '''
    <g id="mouth" style="isolation:isolate">
      {content}
    </g>
    '''

  name = MOUTH.CHEEKY
  svg = CHEEKY_SVG
