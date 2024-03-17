
""" instabot is a tool which used for the instagram automation """

""" step-1: install package instabot using pip install instabot"""


from instabot import Bot
bot=Bot()
bot.login(username="user_name_of_yours",password='password_of_ur_account')


''' syntax to follow someone '''
#bot.follow('enter_user_id_to_follow')



''' syntax to unfollow someone '''
#bot.unfollow('enter_user_id_to_follow')


''' syntax to upload photo '''
#bot.upload_photo(path_of_photo)


''' syntax to message someone '''
#bot.send_message("message to send",["enter user id to send "])



''' syntax TO show the followers list '''

'''followers=bot.get_user_followers("enter user id to send ")
for follower in followers:
    print(bot.get_user_info(follower))'''
