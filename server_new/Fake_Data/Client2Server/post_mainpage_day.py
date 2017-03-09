import json
import datetime


post_mainpage_day = {
    'users':
    {
        'uid': 0

    },
    'date': {'date': "2017-03-08", 'id': 0},
    'blocks': [
        {'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 0, 'id': 0},
        {'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 47, 'id': 47}
    ]

}


print(json.dumps(post_mainpage_day))
