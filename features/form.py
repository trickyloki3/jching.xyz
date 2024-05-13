import os
import uuid
import json

def put_form(form_dir, form_data, max_file_count = 1000):
    if len(os.listdir(form_dir)) >= max_file_count:
        raise Exception('reached max file count')

    with open(os.path.join(form_dir, str(uuid.uuid4())), 'w') as output:
        json.dump(form_data, output, indent = 4)
