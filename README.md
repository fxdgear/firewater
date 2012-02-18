# Firewater

Why firewater, well I was thinking about calling this fire-c then fire-sea then firewater. So there ya go.

## Requirements

* [Twisted](http://twistedmatrix.com/)
* [Pyfire](https://github.com/mariano/pyfire)

## Installation

There's really nothing to install except the requirements.

## Setup

In `settings.py` put in your campfire info and IRC info.

    # Campfire Settings
    SUBDOMAIN = ""  # if your camfire url is awesomebusiness.campfirenow.com then your submain is awesomebusiness
    USERNAME = ""  # username you login to campfire with
    PASSWORD = ""  # password
    ROOM_NAME = ""  # the name of the room your joining. (including spaces if they're their)
    REAL_NAME = ""  # Your name as it appears in the "Who's here?" secion of the campfire room

    # IRC Settings
    IRC_NAME = ""  # name that IRC bot will take when joining the IRC room
    IRC_ROOM = ""  # IRC room to join
    IRC_SERVER = "irc.freenode.net"  # if you're using soemthing than freenode, put it here
    IRC_PORT = 6667  # same goes for your port number

##  Running firewater

in the firewater directory run ``python bot.py``. If you like you can `tail -f foo` to follow the log and see what's going on with the bot.

The bot will join both your camfire room and your irc room.

Any messages said in Campfire will show up in IRC as: [Persons Name] what they said
Any message sent from IRC will show up in Campfire as though you were there and you said it yourself.

## Problems

1. The program doesn't exit gracefully. Something in the campfire stream is not exiting and I havne't had time to look at it yet.  
2. Messages sent from campfire to IRC are SLOW they arrive seconds after the message is sent, but then when they get sent to IRC something is going on and the message is not being immidiatly sent into IRC.
