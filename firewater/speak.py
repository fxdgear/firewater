import pyfire
from firewater.settings import SUBDOMAIN, USERNAME, PASSWORD, ROOM_NAME


campfire = pyfire.Campfire(SUBDOMAIN, USERNAME, PASSWORD, ssl=True)
room = campfire.get_room_by_name(ROOM_NAME)
room.join()
message = raw_input("Enter your message --> ")
if message:
    room.speak(message)
room.leave()
