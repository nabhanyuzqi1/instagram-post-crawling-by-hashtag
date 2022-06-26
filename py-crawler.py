import instaloader
bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, 'yuzqialmbrk')
print(type(profile))

# Instagram Handle and Profile ID
print("Username:", profile.username)
print("User ID", profile.userid)
# Number of Followers and Followees
print("# of followers:", profile.followers)
print("# of followees", profile.followees)


hashtag = instaloader.Hashtag.from_name(bot.context, 'data_mining')
python_posts = hashtag.get_posts()

for index, post in enumerate(python_posts, 1):
    bot.download_post(post, target=f'{hashtag.name}_{index}')

    
    print(hashtag)
