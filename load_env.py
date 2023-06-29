from dotenv import load_dotenv
import os

load_dotenv()

sc_token = os.environ.get("SC_TOKEN")
tg_token = os.environ.get("TG_TOKEN")