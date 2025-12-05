import os
import dotenv




dotenv.load_dotenv()

token = os.getenv("TOKEN")
admin_ids = {7075258047, 2022851663}
my_id = os.getenv("MY_ID")