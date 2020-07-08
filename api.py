import vk

token = '<access_token>'

session = vk.Session(access_token=token)
api = vk.API(session, v="5.95")
api.account.setOnline(voip=0)
