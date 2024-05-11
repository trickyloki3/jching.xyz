import os
import yaml
import markdown

def get_post_list(post_dir):
    post_list = []

    for post_file in os.listdir(post_dir):
        if post_file.endswith('.yaml'):
            post_list.append(get_post(os.path.join(post_dir, post_file)))

    # sort post list by date in descending order
    post_list.sort(key = lambda x: x['date'], reverse = True)

    return post_list

def get_post(post_file):
    with open(post_file) as input:
        post = yaml.safe_load(input)

        return {
            'tag': post['tag'],
            'meta': post['meta'],
            'date': post['date'],
            'post': markdown.markdown(post['post'])
        }
