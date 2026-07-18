from datetime import datetime
import random

def generate_email():
    cur_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return f"test_ash_{cur_time}{random.randint(1, 99)}@gmail.com"