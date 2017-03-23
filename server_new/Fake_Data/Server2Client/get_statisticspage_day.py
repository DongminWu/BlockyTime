import json
import datetime


get_statisticspage_day = {
    'users':
    {
        'uid': 0,
        'nick_name': 'pipicold'

    },
    'statistics': {
        'Day':
        [
            {
                'primary_id': 0,

                'hours': 3.5,
                'presentage': 70,
                'secondary_category': [
                    {'secondary_id': 0,
                     'hours': 3.5,
                     'presentage': 35},
                    {'secondary_id': 1,
                     'hours': 3.5,
                     'presentage': 35}
                ]

            },
            {
                'primary_id': 1,

                'hours': 3.5,
                'presentage': 30,
                'secondary_category': [
                    {'secondary_id': 3,
                     'hours': 3.5,
                     'presentage': 25},
                    {'secondary_id': 2,
                     'hours': 3.5,
                     'presentage': 5}
                ]

            }
        ]
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


print(json.dumps(get_statisticspage_day))
