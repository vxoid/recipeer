from recipe import *
import requests

def search_recipe(query: str) -> List[int]:
  response = requests.get(f"{SC_API}/recipes/complexSearch?query={query}&number=50&apiKey={sc_token}")
  response.raise_for_status()
  dict = response.json()

  recipe_ids = [recipe["id"] for recipe in dict["results"]]
  
  return recipe_ids

def get_random_recipe() -> int:
  response = requests.get(f"{SC_API}/recipes/random?number=1&apiKey={sc_token}");
  response.raise_for_status()
  dict = response.json()

  recipe_id = dict["recipes"][0]["id"]

  return recipe_id