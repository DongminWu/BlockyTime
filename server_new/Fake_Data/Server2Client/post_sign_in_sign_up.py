import json
import datetime


post_sign_in_sign_up = {
    'users':
    {
        'uid': 0,
        'nick_name': 'pipicold'

    },
    'status':1,
    'redirect_url':'http://www.myurl.com/mainpage.html'

}


print(json.dumps(post_sign_in_sign_up))
