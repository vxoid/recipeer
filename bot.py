from telegram.ext import *
from spoonacular import *
from telegram import *
import random as rand
import re

def remove_wrapped_text(text: str) -> str:
  pattern = r"<.*?>"
  cleaned_text = re.sub(pattern, "\n", text)
  return cleaned_text

def reply_recipe(message: Message, recipe: Recipe):
  proteins = recipe.get_proteins()
  calories = recipe.get_calories()
  ingredients = "\n".join([f"{ingredient._original}" for ingredient in recipe._ingredients])

  details = f"""
{recipe._title} 😋

Ingredients 🥒:
{ingredients}

Nutrients:
{proteins[0]} {proteins[1]} of proteins 💪
{calories[0]} {calories[1]} ⚡
  """

  msg = message.reply_photo(
    recipe._image,
    details
  )

  details = f"""
Instructions:
{remove_wrapped_text(recipe._instructions)}

😋Good luck.
  """

  msg.reply_text(
    details
  )


def random(update: Update, context: CallbackContext):
  id = get_random_recipe()
  recipe = Recipe(id)

  reply_recipe(update.message, recipe)

def search(update: Update, context: CallbackContext):
  if len(context.args) < 1:
    update.message.reply_text(f"Enter a query please")
    return
  
  query = context.args[0]

  ids = search_recipe(query)
  if len(ids) < 1:
    update.message.reply_text(f"No results by query '{query}' 😭")
    return

  recipe = Recipe(rand.choice(ids))

  reply_recipe(update.message, recipe)

updater = Updater(tg_token, use_context=True)
updater.dispatcher.add_handler(CommandHandler("random", random))
updater.dispatcher.add_handler(CommandHandler("search", search, pass_args=True))

updater.start_polling()