import os
from ringcentral import SDK


accountId = '279193004'
extensionId = '279193004'




def send_sms(req):
    body = {
    'from': {
    'phoneNumber': '+19293141718'
    },
    'to': [
    {
    'phoneNumber': req['phone']
    }
    ],
    'text': req['message']
    }
    rcsdk = SDK('qQ68acHFT3GS2QnAMuHgiw', 'Pg9yu1F4QLiSWohD6UlFUA9zd1nIG-SDCtfhcjSJxiLg', 'https://platform.devtest.ringcentral.com')
    platform = rcsdk.platform()
    platform.login('+19293141718', '101', 'welcomeKK@2020')
    r =platform.post(f'/restapi/v1.0/account/'+accountId+'/extension/'+extensionId+'/sms', body)
    return {"statusCode":201, "message":"Sms sent successfully"}
