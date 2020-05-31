import vk_api
import time
import random

token = "8587a3f4d8d512ea52af80fb1ba7b48a35451ed35ac32e4bb20c68d581016c23310f09543689bf2cca707"

vk = vk_api.VkApi(token="8587a3f4d8d512ea52af80fb1ba7b48a35451ed35ac32e4bb20c68d581016c23310f09543689bf2cca707")
def register_new_user(user_id):
    c.execute("INSERT INTO users(user_id, state) VALUES(%d, '')" % user_id)
    conn.commit()
    c.execute("INSERT INTO users_info(user_id, user_wish, user_image state) VALUES(%d, '')" % user_id)
    conn.commit()


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "Что умеешь?":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Не много", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "":
                vk.method("messages.send",
                          {"peer_id": id, "message": "ок", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "пока":
                vk.method("messages.send", {"peer_id": id, "message": "Пока! Возвращайся ещё!",
                                            "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Этой команды я пока что не знаю, но может скоро узнаю!",
                           "random_id": random.randint(1, 2147483647)})
            vk._auth_token()
            result = vk_session.method("messages.getById",
                               {"message_id": [event.message_id],
                                          "group_id": 195412815
            })
            print(result)


            #try:
                #photo = result['items'][0]['attachments'][0]['photo']
                #attachment = "photo{}_{}_{}".format(photo['owner_id'], photo['id'], photo['access_key'])
            #except:
                #attachment = None


            #vk.messages.send(
                #user_id=event.user_id,
                #message="Привет!",
                #keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                #random_id = random_id()
            )
    #except Exception as E:
        #time.sleep(1)

