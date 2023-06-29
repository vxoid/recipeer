from ingredient import *
from nutrient import *
from load_env import *
from typing import *
from consts import *
import requests

class Recipe:
  def __init__(self, id: int):
    response = requests.get(f"{SC_API}/recipes/{id}/information?apiKey={sc_token}&includeNutrition=true")
    response.raise_for_status()

    dict = response.json()
    self._id = dict["id"]
    self._title = dict["title"]
    self._image = dict["image"]
    self._image_type = dict["imageType"]
    self._ready_in_minutes = dict["readyInMinutes"]
    self._instructions = dict["instructions"]
    self._health_score = dict["healthScore"]
    self._nutrients = [
      Nutrient(
        nutrient["name"],
        nutrient["amount"],
        nutrient["unit"],
        nutrient["percentOfDailyNeeds"]
      ) for nutrient in dict["nutrition"]["nutrients"]
    ]

    self._ingredients = [
      Ingredient(
        ingredient["id"],
        ingredient["amount"],
        ingredient["image"],
        ingredient["name"],
        ingredient["unit"],
        ingredient["original"]
      ) for ingredient in dict["extendedIngredients"]
    ]

  def get_calories(self) -> Tuple[float, str]:
    return [(nutrient._amount, nutrient._unit) for nutrient in self._nutrients if nutrient._name == "Calories"][0]
  
  def get_proteins(self) -> Tuple[float, str]:
    return [(nutrient._amount, nutrient._unit) for nutrient in self._nutrients if nutrient._name == "Protein"][0]

  def __str__(self) -> str:
    return f"Recipe ( id: {self._id}, title: {self._title}, image: {self._image}, health_score: {self._health_score}, ingredients: {[str(ingredient) for ingredient in self._ingredients]}, nutrients: {[str(nutrient) for nutrient in self._nutrients]} )"