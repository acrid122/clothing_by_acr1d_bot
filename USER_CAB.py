import vk_api
import json
from VK_CREDITS import *
from FIRST_KEYBOARD import *
from KEYBOARD_TYPE_EVENT import *
from main import *
import sqlite3 as sq
import requests
from USERS_DB import *
import asyncio


class USER_CAB:
    def __init__(self, user_id):
        self.USER_ID = user_id
    def __changeEmailData__(self, vk_session, text):
        sendMessage(self.USER_ID, {'message': 'Введите новый email в формате ***@**.** в ответ на это сообщение'}, vk_session)
    def __changePhoneData__(self, vk_session, text):
        sendMessage(self.USER_ID, {'message': 'Введите новый телефон в формате +7********** в ответ на это сообщение'}, vk_session)
    def __changeDeliveryAddressData__(self, vk_session, text):
        sendMessage(self.USER_ID, {'message': 'Введите новый адрес доставки в формате г. ****, ул. ****, д. * в ответ на это сообщение'}, vk_session)
    def __changeFIOData__(self, vk_session, text):
        sendMessage(self.USER_ID, {'message': 'Введите новые ФИО в формате Фффф Ииии Оооо в ответ на это сообщение'}, vk_session)
