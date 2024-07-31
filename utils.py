from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('')
        params = {
            'sender': '2000500666',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f' کد تایید شما{code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
