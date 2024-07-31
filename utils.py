from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('5A6D7434655A492F564F695363784F4679586E43684F4E4B70723934353561466A7736304B444948717A4D3D')
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
