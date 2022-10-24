from requests import post
print("start bot")
Day = 1
while True :
    post(f"https://graph.facebook.com/109479985286814/photos?url=https://i.ibb.co/tz2W7HX/FB-IMG-16663953467762068.jpg&message={Day}&access_token=EAALXMZAnZAkFUBADyDbCjRN2ZCqiDXLjwxCSMmSEPeNAyn2iJcF8gzmfq5z3aZCuDCD29M3cq6Y6YKIqCetY8Fdn7DUcQhbMimJwqlCoN0VP32O44MfJUs7rYhcWdqMXihjSNHZCYjZBR2c7ORr9vis5QOjZAqG8ZBVtMOjype0VsEr61YWJzwrrAMwkL1aLl2cEZAO1e3AayuQZDZD")
    Day += 1
    time.sleep(60*60*24)
