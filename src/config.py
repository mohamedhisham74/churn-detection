import os
from dotenv import Load_dotenv 
import joblip 

Load_dotenv(override=True)

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("APP_VERSION")
SECRET_KEY_TOKEN= os.getenv("API_SECRET_KEY")


BASE_DIR=os.dirname(os.path.dirname(os.path.abspath(__file__)))

ARTIFAVTS_FOLDER_PATH=os.path.join(BASE_DIR,"artifacts")

preproccessor = joblip.load(os.path.join(ARTIFAVTS_FOLDER_PATH,'preporcessor.pkl'))
model = joblip.load(os.path.join(ARTIFAVTS_FOLDER_PATH,'forest_tuned.pkl'))

