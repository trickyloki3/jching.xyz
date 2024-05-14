import os
import uuid
import json

def put_form(folder, form, max_file_count = 100):
    if len(os.listdir(folder)) >= max_file_count:
        raise Exception('exceeded max file count')

    with open(os.path.join(folder, str(uuid.uuid4())), 'w') as output:
        json.dump(form, output, indent = 4)
