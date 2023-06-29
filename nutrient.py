class Nutrient:
  def __init__(self, name: str, amount: float, unit: str, percent_of_daily_need: float):
    self._name = name
    self._amount = amount
    self._unit = unit
    self._percent_of_daily_need = percent_of_daily_need

  def __str__(self) -> str:
    return f"Nutrient ( name: {self._name}, amount: {self._amount}, unit: {self._unit} )"