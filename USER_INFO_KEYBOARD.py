###USER_INFO_KEYBOARD
from vk_api.bot_longpoll import *
from vk_api.keyboard import *
from KEYBOARD_TYPE_EVENT import *
def user_info_keyboard():
   key_board = VkKeyboard(one_time = False, inline = False)
   key_board.add_button(
    label="Информация об аккаунте",
    color=VkKeyboardColor.POSITIVE,
    payload={'button': 6}
   )
   key_board.add_button(
    label = "Изменить данные",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 7}
   )
   key_board.add_line()
   key_board.add_button(
    label = "Текущая сумма корзины",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 8}
   )
   key_board.add_line()
   key_board.add_button(
    label = "История заказов",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 9}
   )
   key_board.add_button(
       label="Назад",
       color=VkKeyboardColor.SECONDARY,
       payload={'button': 10}
   )
   return key_board.get_keyboard()
def change_data_keyboard():
   key_board = VkKeyboard(one_time = False, inline = False)
   key_board.add_button(
    label = "Изменить почту",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 11}
   )
   key_board.add_button(
    label = "Изменить номер телефона",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 12}
   )
   key_board.add_line()
   key_board.add_button(
    label = "Изменить адрес доставки",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 13}
   )
   key_board.add_button(
    label = "Изменить ФИО",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 14}
   )
   key_board.add_line()
   key_board.add_button(
       label = "Назад",
       color=VkKeyboardColor.SECONDARY,
       payload={'button': 15}
   )
   return key_board.get_keyboard()
