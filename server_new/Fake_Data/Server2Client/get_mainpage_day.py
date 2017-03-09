import json
import datetime


get_mainpage_day = {
    'users':
    {
        'uid': 0,
        'nick_name': 'pipicold'

    },
    'date': {'date': "2017-03-08", 'id': 0, 'last_changed_time': "2017-03-08 16:43:32", 'uid': 0},
    'statics': {
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
    ],
    'blocks': [
        {'display_time': u'00:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 0, 'date_id': 0, 'id': 0},
        {'display_time': u'00:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 1, 'date_id': 0, 'id': 1},
        {'display_time': u'01:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 2, 'date_id': 0, 'id': 2},
        {'display_time': u'01:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 3, 'date_id': 0, 'id': 3},
        {'display_time': u'02:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 4, 'date_id': 0, 'id': 4},
        {'display_time': u'02:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 5, 'date_id': 0, 'id': 5},
        {'display_time': u'03:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 6, 'date_id': 0, 'id': 6},
        {'display_time': u'03:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 7, 'date_id': 0, 'id': 7},
        {'display_time': u'04:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 8, 'date_id': 0, 'id': 8},
        {'display_time': u'04:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 9, 'date_id': 0, 'id': 9},
        {'display_time': u'05:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 10, 'date_id': 0, 'id': 10},
        {'display_time': u'05:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 11, 'date_id': 0, 'id': 11},
        {'display_time': u'06:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 12, 'date_id': 0, 'id': 12},
        {'display_time': u'06:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 13, 'date_id': 0, 'id': 13},
        {'display_time': u'07:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 14, 'date_id': 0, 'id': 14},
        {'display_time': u'07:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 15, 'date_id': 0, 'id': 15},
        {'display_time': u'08:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 16, 'date_id': 0, 'id': 16},
        {'display_time': u'08:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 17, 'date_id': 0, 'id': 17},
        {'display_time': u'09:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 18, 'date_id': 0, 'id': 18},
        {'display_time': u'09:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 19, 'date_id': 0, 'id': 19},
        {'display_time': u'10:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 20, 'date_id': 0, 'id': 20},
        {'display_time': u'10:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 21, 'date_id': 0, 'id': 21},
        {'display_time': u'11:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 22, 'date_id': 0, 'id': 22},
        {'display_time': u'11:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 23, 'date_id': 0, 'id': 23},
        {'display_time': u'12:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 24, 'date_id': 0, 'id': 24},
        {'display_time': u'12:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 25, 'date_id': 0, 'id': 25},
        {'display_time': u'13:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 26, 'date_id': 0, 'id': 26},
        {'display_time': u'13:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 27, 'date_id': 0, 'id': 27},
        {'display_time': u'14:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 28, 'date_id': 0, 'id': 28},
        {'display_time': u'14:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 29, 'date_id': 0, 'id': 29},
        {'display_time': u'15:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 30, 'date_id': 0, 'id': 30},
        {'display_time': u'15:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 31, 'date_id': 0, 'id': 31},
        {'display_time': u'16:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 32, 'date_id': 0, 'id': 32},
        {'display_time': u'16:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 33, 'date_id': 0, 'id': 33},
        {'display_time': u'17:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 34, 'date_id': 0, 'id': 34},
        {'display_time': u'17:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 35, 'date_id': 0, 'id': 35},
        {'display_time': u'18:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 36, 'date_id': 0, 'id': 36},
        {'display_time': u'18:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 37, 'date_id': 0, 'id': 37},
        {'display_time': u'19:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 38, 'date_id': 0, 'id': 38},
        {'display_time': u'19:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 39, 'date_id': 0, 'id': 39},
        {'display_time': u'20:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 40, 'date_id': 0, 'id': 40},
        {'display_time': u'20:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 41, 'date_id': 0, 'id': 41},
        {'display_time': u'21:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 42, 'date_id': 0, 'id': 42},
        {'display_time': u'21:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 43, 'date_id': 0, 'id': 43},
        {'display_time': u'22:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 44, 'date_id': 0, 'id': 44},
        {'display_time': u'22:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 45, 'date_id': 0, 'id': 45},
        {'display_time': u'23:00', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 46, 'date_id': 0, 'id': 46},
        {'display_time': u'23:30', 'uid': 0, 'secondary_category_id': 0,
         'primary_category_id': 0, 'position': 47, 'date_id': 0, 'id': 47}
    ]

}


print(json.dumps(get_mainpage_day))
