import random
import string

def generate_project_id():
      return random.randint(100, 999)

def generate_employee_id(length):
      letters_and_digits = string.ascii_letters + string.digits
      result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
      return result_str