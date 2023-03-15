import schedule
import vk_api
import json
from VK_CREDITS import *
from KEYBOARD_TYPE_EVENT import *
import sqlite3 as sq
import requests
from USERS_DB import *
import re
import asyncio
#from vkbottle import *
#import schedule

class GROUP_W:
  def __init__(self, GROUP_ID, GROUP_TOKEN):
    self.GROUP_ID = GROUP_ID
    self.GROUP_TOKEN = GROUP_TOKEN
  #Set VK Session
  def __vkBotSession__(self):
    self.VK_SESSION = vk_api.VkApi(token = self.GROUP_TOKEN)
    return self.VK_SESSION
  #LongPoll
  def __vkLongPoll__(self, vk_session, group_id):
    longpoll = VkBotLongPoll(self.VK_SESSION, self.GROUP_ID)
    return longpoll

  
class USER_W:
  def __init__(self, VK_SESSION, lonpoll):
    self.VK_SESSION = VK_SESSION
    self.longpoll = longpoll
  #Getting message from users
  def __userWork__(self):
      for event in self.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
          self.USER_MESSAGE = event.object.message['text']
          self.USER_ID = event.object.message['from_id']
          getUserMessage(self.USER_MESSAGE)
          print(event.object.message)
          if checkInUSERS_DB(self.USER_ID):
            insertUserToUSERS_DB(self.USER_ID)
            sendMessage(self.USER_ID, {'message': 'Привет! На связи clothing by acr1d_!' + '\n' * 4 +
                                       'Для оформления заказа Вам необходимо указать некоторые данные в следующем формате:' + '\n' * 4 +
                                       'Email: ****@***.***' + '\n' +
                                       'Телефон: +7**********' + '\n' +
                                       'Адрес доставки: г. *****, ул. ******, д. *****' + '\n' +
                                      'ФИО: **** **** ****' + '\n' * 4 +
                                       'Предоставляя следующие данные, Вы соглашаетесь с политикой конфиденциальности.' + '\n' +
                                       'Политика конфиденциальности доступна в разделе FAQ -> Политика конфиденциальности' + '\n' * 2 +
                                       'Пример заполнения:', 'keyboard': first_key_board(),
                                       'attachment': getPhotoAttachment(self.USER_ID, 'form_example.gif', self.VK_SESSION)},
                                        self.VK_SESSION)
            sendMessage(self.USER_ID, {'message': 'Шаблон для регистрации' + '\n' +
                                       'Email:' + '\n' +
                                       'Телефон:' + '\n' +
                                       'Адрес доставки:' + '\n' +
                                       'ФИО:'}, self.VK_SESSION)
          if 'Email:' in self.USER_MESSAGE and 'Телефон:' in self.USER_MESSAGE and 'Адрес доставки:' in self.USER_MESSAGE and 'ФИО:' in self.USER_MESSAGE:
            self.EMAIL = self.USER_MESSAGE[self.USER_MESSAGE.find('Email:') + 7: self.USER_MESSAGE.find('Телефон:') - 1]
            self.PHONE = self.USER_MESSAGE[self.USER_MESSAGE.find('Телефон:') + 9: self.USER_MESSAGE.find('Адрес доставки:') - 1]
            self.DELIVERY_ADDRESS = self.USER_MESSAGE[self.USER_MESSAGE.find('Адрес доставки:') + 16 : self.USER_MESSAGE.find('ФИО:') - 1]
            self.FIO = self.USER_MESSAGE[self.USER_MESSAGE.find('ФИО:') + 5:]
            if checkDataCorrect(self.EMAIL, self.DELIVERY_ADDRESS, self.PHONE, self.FIO) == "":
                updateUserInfoInUSERS_DB(str(self.USER_ID), self.EMAIL, self.DELIVERY_ADDRESS, self.PHONE, self.FIO)
                sendMessage(self.USER_ID, {'message': 'Спасибо за регистрацию!'}, self.VK_SESSION)
            else:
                sendMessage(self.USER_ID, {'message': checkDataCorrect(self.EMAIL, self.DELIVERY_ADDRESS, self.PHONE, self.FIO) +
                                                      'Проверьте корректность введенных данных!' + '\n' * 2 +
                                                      'Шаблон для регистрации' + '\n' +
                                                      'Email:' + '\n' +
                                                      'Телефон:' + '\n' +
                                                      'Адрес доставки:' + '\n' +
                                                      'ФИО:'}, self.VK_SESSION)
            #Обработка изменения учетных данных
          if 'reply_message' in event.object.message:
            if '-' + str(GROUP_ID) == str(event.object.message['reply_message']['from_id']):
                get_user_info_frbd = getUserInUSERS_DB(str(self.USER_ID))
                if event.object.message['reply_message']['text'].find('Введите новый email в формате ***@**.** в ответ на это сообщение') != -1:
                    if checkDataCorrect(self.USER_MESSAGE, get_user_info_frbd[1], get_user_info_frbd[2], get_user_info_frbd[3]) == "":
                        updateUserEmailDataInUSERS_DB(str(self.USER_ID), self.USER_MESSAGE)
                        sendMessage(self.USER_ID, {'message': 'Почта обновлена!'}, self.VK_SESSION)
                    else:
                        sendMessage(self.USER_ID, {'message': 'Почта введена в неверном формате! Введите новый email в формате ***@**.** в ответ на это сообщение'}, self.VK_SESSION)
                elif event.object.message['reply_message']['text'].find('Введите новый телефон в формате +7********** в ответ на это сообщение') != -1:
                    if checkDataCorrect(get_user_info_frbd[0], get_user_info_frbd[1], self.USER_MESSAGE, get_user_info_frbd[3]) == "":
                        updateUserPhoneNumberDataInUSERS_DB(str(self.USER_ID), self.USER_MESSAGE)
                        sendMessage(self.USER_ID, {'message': 'Номер телефона обновлен!'}, self.VK_SESSION)
                    else:
                        sendMessage(self.USER_ID, {'message': 'Номер телефона введен в неверном формате! Введите новый телефон в формате +7********** в ответ на это сообщение'},self.VK_SESSION)
                elif event.object.message['reply_message']['text'].find('Введите новый адрес доставки в формате г. ****, ул. ****, д. * в ответ на это сообщение') != -1:
                    if checkDataCorrect(get_user_info_frbd[0], self.USER_MESSAGE, get_user_info_frbd[2], get_user_info_frbd[3]) == "":
                        updateUserDeliveryAddressDataInUSERS_DB(str(self.USER_ID), self.USER_MESSAGE)
                        sendMessage(self.USER_ID, {'message': 'Адрес доставки обновлен!'}, self.VK_SESSION)
                    else:
                        sendMessage(self.USER_ID, {'message': 'Адрес доставки введен в неверном формате! Введите новый адрес доставки в формате г. ****, ул. ****, д. * в ответ на это сообщение'},self.VK_SESSION)
                elif event.object.message['reply_message']['text'].find('Введите новые ФИО в формате Фффф Ииии Оооо в ответ на это сообщение') != -1:
                    if checkDataCorrect(get_user_info_frbd[0], get_user_info_frbd[1], get_user_info_frbd[2], self.USER_MESSAGE) == "":
                        updateUserFioDataInUSERS_DB(str(self.USER_ID), self.USER_MESSAGE)
                        sendMessage(self.USER_ID, {'message': 'ФИО обновлены!'}, self.VK_SESSION)
                    else:
                        sendMessage(self.USER_ID, {'message': 'ФИО введены в неверном формате! Введите новые ФИО в формате Фффф Ииии Оооо в ответ на это сообщение'},self.VK_SESSION)
          if 'payload' in event.object.message:  
            sendPayload(event.object.message, self.VK_SESSION)


def checkDataCorrect(email, delivery_address, phone_number, fio):
    incorrect_info_str = ""
    new_email_set_info = (len(re.findall(r".+@\w+\.\w+", email)) == 1)
    new_phone_number_set_info = (len(re.findall(r"\+7\d{10}", phone_number)) == 1)
    new_delivery_address_set_info = (len(re.findall(r"г\.\s([а-яА-Я]+),\sул\.\s([а-яА-Я]+),\sд\.\s\d+", delivery_address)) == 1)
    new_fio_set_info = (len(re.findall(r"^(([А-Я]{1}[а-яё]{1,23})\s){2}([А-Я]{1}[а-яё]{1,23})$", fio)) == 1)
    if not new_email_set_info:
        incorrect_info_str += "Почта введена в неверном формате!" + '\n'
    if not new_phone_number_set_info:
        incorrect_info_str += "Номер телефона введен в неверном формате!" + '\n'
    if not new_delivery_address_set_info:
        incorrect_info_str += "Адрес доставки введен в неверном формате!" + '\n'
    if not new_fio_set_info:
        incorrect_info_str += "ФИО введены в неверном формате!" + '\n'
    return incorrect_info_str


#Return user message
def getUserMessage(message):
  return message


#Send payload to keyboard  
def sendPayload(ev, vk_session):
  callKeyboard(ev['from_id'], ev['payload'], ev['text'], vk_session)

  
#Set sending messages
def sendMessage(user_id, message, vk_session):
    message_payload = {'user_id': user_id, 'random_id': 0, **message}
    vk_session.method('messages.send', message_payload)


#Send photo
def getPhotoAttachment(user_id, pic, vk_session):
   #vkbottle api
    '''bot = Bot(GROUP_TOKEN)
    doc_uploader = DocMessagesUploader(bot.api)
    doc_gif =  doc_uploader.upload(
        file_source = pic,
        peer_id = '439450094',
      )'''
    upload_address = vk_session.method("docs.getMessagesUploadServer", {'type': 'doc', 'peer_id': user_id})
    request_file = requests.post(upload_address['upload_url'], files = {'file': open(pic, 'rb')}).json()
    save_file = vk_session.method("docs.save", {'file': request_file['file']})
    return f"doc{save_file['doc']['owner_id']}_{save_file['doc']['id']}"
    #VkUpload photo upload
    '''upload = vk_api.VkUpload(vk_session.get_api())
    photo = upload.photo_messages(pic)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f"photo{owner_id}_{photo_id}_{access_key}"  
    return attachment'''



#Check if full info about user is in USERS_DB
def checkFullInfoInUSERS_DB(user_id, vk_session):
    if getUserInUSERS_DB(user_id) == ['0','0','0','0']:
        sendMessage(user_id, {'message': 'Не забудьте зарегистрироваться, чтобы оформить заказ! Данное уведомление приходит раз в сутки.'}, vk_session)


if __name__ == "__main__":
  GROUP_W = GROUP_W(GROUP_ID, GROUP_TOKEN)
  longpoll = GROUP_W.__vkLongPoll__(GROUP_W.__vkBotSession__(), GROUP_W.GROUP_ID)
  USER_W = USER_W(GROUP_W.VK_SESSION, longpoll)
  USER_W.__userWork__()
