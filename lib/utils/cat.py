from lib.utils.utils import Utils


class CatUtils:
  @staticmethod
  def get_random_body_name():
    values = [
        'flame',
        'grassy',
    ]

    return Utils.get_list_random_element(values)

  @staticmethod
  def get_random_eye_shape_name():
    values = [
        'simple',
        'slyboots',
        'stunned',
        # 'swarley',
    ]

    return Utils.get_list_random_element(values)

  @staticmethod
  def get_random_mouth_name():
    values = [
        'impish',
        'majestic',
        # 'moue',
        # 'pouty',
    ]

    return Utils.get_list_random_element(values)
