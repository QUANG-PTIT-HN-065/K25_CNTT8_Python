import random
import string as st


def generate_assignment_code():
    code = "".join(random.choices(st.ascii_uppercase + st.digits, k=4))
    return "PY-" + code
