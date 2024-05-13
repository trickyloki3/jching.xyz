import os
import uuid
import json

def put_form(form_dir, form_data):
    with open(os.path.join(form_dir, str(uuid.uuid4())), 'w') as output:
        json.dump(form_data, output, indent = 4)
