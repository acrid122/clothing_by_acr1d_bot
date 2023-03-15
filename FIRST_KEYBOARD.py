###MAIN KEYBOARD
from vk_api.bot_longpoll import *
from vk_api.keyboard import *
from KEYBOARD_TYPE_EVENT import *
def first_key_board():
   key_board = VkKeyboard(one_time = False, inline = False)
   key_board.add_button(
    label = "Выбор одежды",
    color=VkKeyboardColor.PRIMARY,
    payload={'button': 1}
   )
   key_board.add_line()
   key_board.add_button(
    label = "Мой кабинет",
    color=VkKeyboardColor.POSITIVE,
    payload={'button': 2}
   )
   key_board.add_line()
   key_board.add_button(
    label = "Отследить мою покупку",
    color=VkKeyboardColor.NEGATIVE,
    payload={'button': 3}
   )
   key_board.add_line()
   key_board.add_button(
    label = "Корзина",
    color=VkKeyboardColor.SECONDARY,
    payload={'button': 4}
   )
   key_board.add_button(
    label = "FAQ",
    color=VkKeyboardColor.SECONDARY,
    payload={'button': 5}
   )
   return key_board.get_keyboard()
