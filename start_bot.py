import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import random

import creds




def start():

    # Авторизация
    vk = vk_api.VkApi(token=creds.TOKEN)
    longpoll = VkLongPoll(vk)
    upload = VkUpload(vk)
    vk = vk.get_api()

    # Основной цикл бота
    for event in longpoll.listen():
        if event.to_me:
            print()
            print(dir(event))
            print(event.user_id)
            print(event.text)
            print(event.datetime)
            print(event.attachments)
            print(event.message_flags)
            print(event.flags)

start()


