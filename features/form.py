import os
import uuid
import json

def put_form(folder, group, form, max_file_count = 100):
    path = os.path.join(folder, group)

    if len(os.listdir(path)) >= max_file_count:
        raise Exception('exceeded max file count')

    with open(os.path.join(path, str(uuid.uuid4())), 'w') as output:
        json.dump(form, output, indent = 4)
