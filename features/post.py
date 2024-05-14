import os
import yaml
import markdown
import itertools

def get_post_dict(folder):
    post_list = get_post_list(folder)

    # stable sort post list by date in descending order
    post_list.sort(key = lambda x: x['date'], reverse = True)

    # index contains all public post (hide = False)
    post_dict = {
        'index': list(filter(lambda x: not x['hide'], post_list))
    }

    # stable sort post list by group
    post_list.sort(key = lambda x: x['group'])
    for group, post_list in itertools.groupby(post_list, lambda x : x['group']):
        post_dict[group] = list(post_list)

    return post_dict;

def get_post_list(folder):
    post_list = []

    for root, _, file_list in os.walk(folder):
        for file in file_list:
            path = os.path.join(root, file)
            if path.endswith('yaml'):
                post_list.append(get_post(path))

    return post_list

def get_post(path):
    with open(path) as input:
        path = path.split('/')[-3:]
        post = yaml.safe_load(input)

        return {
            'group': path[0],
            'column' : path[1],
            'tag': post['tag'],
            'hide' : post['hide'],
            'date': post['date'],
            'post': markdown.markdown(post['post'])
        }

def get_column_list(post_list, tag):
    post_list = list(filter(lambda x: tag in x['tag'], post_list)) if tag else post_list

    column_list = []

    post_list.sort(key = lambda x: x['column'])
    for _, post_list in itertools.groupby(post_list, lambda x : x['column']):
         column_list.append(list(post_list))

    return column_list
