from wxpy import *
import requests

bot = Bot(cache_path=True)

tuling = Tuling(api_key='239eda9d867a4ab180a59bd95b7f106e')


"""
bot.self.send('Hello World!1')
bot.file_helper.send('Hello you!1')
"""

# define particular friend
my_friend = bot.friends().search(u'学神牛')[0]
#all_friend = bot.friends()


#my_friend.send('Hello, zhaozhao')
#my_friend.send_image('1.jpg')



# print message
@bot.register()
def print_others(msg):
    print(msg)


group = bot.groups().search('2018 Fall')

# reply particular defined friend before
@bot.register(msg_types=TEXT)
def reply_my_friend(msg):
    if msg.text.lower() == '123':
        msg.sender.send('wuutt')
        group[0].add_members(my_friend,use_invitation=True)
        msg.sender.send('wuutt22')
    else:
        return u'收到: '+msg.text
    #if valid_msg(msg):
     #   invite(msg.sender)
    #if msg=='租房群':
     #   invite(all_friend)
    #else:
     #   tuling.do_reply(msg)


def valid_msg(msg):
    return '租房群' in msg.text.lower()

def invite(user):
    group = bot.groups().search('2018 Fall 租房群DeAnza Foothill')
    group[0].add_member(user,use_invitation=True)


# replay at message in a group
@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        msg.reply(msg.text)


# accept new friend
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = msg.card.accept()
    new_friend.send('1234')
    new_friend.send(new_friend_message())


def new_friend_message():
    msg = 'Hello,欢迎添加微信小助手\n' \
          '1.回复‘租房群’邀请加入租房群。\n' \
          '2.回复\n'
    return msg


embed()