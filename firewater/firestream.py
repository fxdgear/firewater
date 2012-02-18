import ipdb
import time
import pyfire
from firewater.settings import SUBDOMAIN, USERNAME, PASSWORD, ROOM_NAME


class FireStream(object):

    def __init__(self, subdomain, username, password, irc_bot, ssl=True):
        self.subdomain = subdomain
        self.username = username
        self.password = password
        self.ssl = ssl
        self.irc_bot = irc_bot
        self.logger = self.irc_bot.logger

        self.campfire = self.login(self.subdomain, self.username, self.password, self.ssl)
        self.logger.log("[connected to campfire at %s]" %
                        time.asctime(time.localtime(time.time())))

    def login(self, subdomain, username, password, ssl):
        return pyfire.Campfire(subdomain, username, password, ssl=ssl)

    def get_room(self, room_name):
        return self.campfire.get_room_by_name(room_name)

    def join_room(self, room_name):
        self.room = self.get_room(room_name)
        self.room.join()
        self.logger.log("[Joined room %s]" % room_name)

    def incoming(self, message):
        """
            Send message to IRC bot
        """
        user = ""
        if message.user:
            user = message.user.name

        if not user == "Mr Awesome":

            time.sleep(2)
            msg = ""

            if message.is_joining():
                msg = "--> %s ENTERS THE ROOM" % user

            elif message.is_leaving():
                msg = "<-- %s LEFT THE ROOM" % user

            elif message.is_tweet():
                msg = "[%s] %s TWEETED '%s' - %s" % (user, message.tweet["user"], message.tweet["tweet"], message.tweet["url"])

            elif message.is_text():
                msg = "[%s] %s" % (user, message.body)

            elif message.is_upload():
                msg = "-- %s UPLOADED FILE %s: %s" % (user, message.upload["name"], message.upload["url"])

            elif message.is_topic_change():
                msg = "-- %s CHANGED TOPIC TO '%s'" % (user, message.body)

            if msg:
                self.irc_bot.message_to_irc(msg)
                self.logger.log("[Campfire] [%s]" % msg)

    def error(e):
        print("Stream STOPPED due to ERROR: %s" % e)
        print("Press ENTER to continue")

    def start_stream(self):
        self.stream = self.room.get_stream(error_callback=self.error, live=False)
        self.stream.attach(self.incoming).start()
        self.logger.log("[Stream Started] at %s " %
            time.asctime(time.localtime(time.time())))

    def stop_stream(self):
        self.stream.stop().join()
        self.logger.log("[Stream Stopped at %s]" %
            time.asctime(time.localtime(time.time())))
        self.room.leave()
        self.logger.log("[Left room %s at %s]" % (ROOM_NAME, time.asctime(time.localtime(time.time()))))


if __name__ == "__main__":
    fs = FireStream(SUBDOMAIN, USERNAME, PASSWORD)
    fs.join_room(ROOM_NAME)
    fs.start_stream()
