###KEYBOARD_TYPE_EVENT
import json
from FIRST_KEYBOARD import first_key_board
from main import *
from USER_INFO_KEYBOARD import *
from USERS_DB import *
from USER_CAB import *


class USER_KEYBOARD_EVENTS:
    def __setKeyboardEventInfo__(self, user_id, payload, text, vk_session):
        KEYBOARD_EVENT_INFO = [user_id, payload, text, vk_session]
        return KEYBOARD_EVENT_INFO
    def __keyboardEvent__(self, user_id, payload, text, vk_session):
        res = json.loads(self.__setKeyboardEventInfo__(user_id, payload, text, vk_session)[1])
        print(res)
        USER_INFO = USER_CAB(user_id)
        if 'button' in res:
            res = res['button']
            if res in [10]:
                sendMessage(user_id, {'message': 'Главное меню', 'keyboard': first_key_board()}, vk_session)
            if res in [2, 15]:
                sendMessage(user_id, {'message': 'Личный кабинет', 'keyboard': user_info_keyboard()}, vk_session)
            if res == 6:
                get_user_info_frbd = getUserInUSERS_DB(str(user_id))
                sendMessage(user_id, {'message': f"Email: {get_user_info_frbd[0]}\nТелефон: {get_user_info_frbd[2]}\nАдрес доставки: {get_user_info_frbd[1]}\nФИО: {get_user_info_frbd[3]}"}, vk_session)
            if res == 7:
                sendMessage(user_id, {'message': 'Изменение данных', 'keyboard': change_data_keyboard()}, vk_session)
            if res == 11:
                USER_INFO.__changeEmailData__(vk_session, text)
            elif res == 12:
                USER_INFO.__changePhoneData__(vk_session, text)
            elif res == 13:
                USER_INFO.__changeDeliveryAddressData__(vk_session, text)
            elif res == 14:
                USER_INFO. __changeFIOData__(vk_session, text)
        del USER_INFO
                
def callKeyboard(user_id, payload, text, vk_session):
    KB_EV = USER_KEYBOARD_EVENTS()
    KB_EV.__keyboardEvent__(user_id, payload, text, vk_session)
    

    
