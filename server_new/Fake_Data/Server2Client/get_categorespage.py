import json
import datetime


get_categoriespage = {
    'users':
    {
        'uid': 0,
        'nick_name': 'pipicold'

    },
    'categories': [
        {'color': u'#f23456', 'id': 0, 'name': u'fake_category0', 'uid': 0,
         'secondary_category': [
             {'primary_id': 0, 'color': u'#b33321', 'id': 0,
              'name': u'fake_secondary0', 'uid': 0},
             {'primary_id': 0, 'color': u'#b33321', 'id': 1,
              'name': u'fake_secondary1', 'uid': 0}

         ]},
        {'color': u'#f23456', 'id': 1, 'name': u'fake_category1', 'uid': 0,
         'secondary_category': [
             {'primary_id': 0, 'color': u'#b33321', 'id': 0,
              'name': u'fake_secondary0', 'uid': 0},
             {'primary_id': 0, 'color': u'#b33321', 'id': 1,
              'name': u'fake_secondary1', 'uid': 0}

         ]}
    ]

}


print(json.dumps(get_categoriespage))
