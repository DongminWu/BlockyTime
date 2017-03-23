import json
import datetime


post_reset_password = {
    'users':
    {
        'nick_name': 'pipicold',
        'password': 'asdfb@adsf',
        'new_passowrd':'abcdefg'

    }

}


print(json.dumps(post_reset_password))
