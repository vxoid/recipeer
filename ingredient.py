class Ingredient:
  def __init__(self, id: int, amount: float, image: str, name: str, unit: str, original: str):
    self._id = id
    self._amount = amount
    self._image = image
    self._name = name
    self._unit = unit
    self._original = original

  def __str__(self) -> str:
    return f"Ingredient ( id: {self._id}, name: {self._name}, image: {self._image}, original: {self._original} )"