"""
Master configuration file for Muddery.

NOTE: NO MODIFICATIONS SHOULD BE MADE TO THIS FILE!

All settings changes should be done by copy-pasting the variable and
its value to <gamedir>/conf/settings.py.

Hint: Don't copy&paste over more from this file than you actually want
to change.  Anything you don't copy&paste will thus retain its default
value - which may change as Muddery is developed. This way you can
always be sure of what you have changed and what is default behaviour.

"""

import os

######################################################################
# Muddery base server config
######################################################################

MUDDERY_DIR = os.path.dirname(os.path.abspath(__file__))

######################################################################
# Django web features
######################################################################

# The name of the currently selected webclient template. This corresponds to the
# directory names shown in the webtemplates directory.
WEBCLIENT_TEMPLATE = 'default'

######################################################################
# Evennia pluggable modules
######################################################################

# The command parser module to use. See the default module for which
# functions it must implement
COMMAND_PARSER = "muddery.server.conf.cmdparser.cmdparser"

######################################################################
# Typeclasses and other paths
######################################################################

# Server-side session class used.
SERVER_SESSION_CLASS = "muddery.server.conf.serversession.ServerSession"

# These are paths that will be prefixed to the paths given if the
# immediately entered path fail to find a typeclass. It allows for
# shorter input strings. They must either base off the game directory
# or start from the evennia library.
TYPECLASS_PATHS = ["muddery.typeclasses"]

# Typeclass for player objects (linked to a character) (fallback)
BASE_PLAYER_TYPECLASS = "muddery.typeclasses.players.MudderyPlayer"
# Typeclass and base for all objects (fallback)
BASE_OBJECT_TYPECLASS = "muddery.typeclasses.objects.MudderyObject"
# Typeclass for character objects linked to a player (fallback)
BASE_CHARACTER_TYPECLASS = "muddery.typeclasses.characters.MudderyCharacter"
# Typeclass for rooms (fallback)
BASE_ROOM_TYPECLASS = "muddery.typeclasses.rooms.MudderyRoom"
# Typeclass for Exit objects (fallback).
BASE_EXIT_TYPECLASS = "muddery.typeclasses.exits.MudderyExit"
# Typeclass for Channel (fallback).
BASE_CHANNEL_TYPECLASS = "muddery.typeclasses.channels.MudderyChannel"
# Typeclass for Scripts (fallback). You usually don't need to change this
# but create custom variations of scripts on a per-case basis instead.
BASE_SCRIPT_TYPECLASS = "muddery.typeclasses.scripts.MudderyScript"
# Typeclass for NPCs
BASE_NPC_TYPECLASS = "muddery.typeclasses.npcs.MudderyNPC"

######################################################################
# World data features
######################################################################

# attribute's category for data info
WORLD_DATA_INFO_CATEGORY = "data_info"

# data app name
WORLD_DATA_APP = "worlddata"

# data file's folder under user's game directory.
WORLD_DATA_FOLDER = "worlddata/data"

# data file's format, only support csv now.
WORLD_DATA_FILE_TYPE = "csv"

# unique rooms
WORLD_ROOMS = ("world_rooms",)

# unique exits
WORLD_EXITS = ("world_exits",)

# unique objects
WORLD_OBJECTS = ("world_objects",)

# details
WORLD_DETAILS = ("world_details",)

# normal objects
PERSONAL_OBJECTS = ("personal_objects",)

# all data models
WORLD_DATA_MODELS = (WORLD_ROOMS,
                     WORLD_EXITS,
                     WORLD_OBJECTS,
                     WORLD_DETAILS,
                     PERSONAL_OBJECTS)

BASE_AUTOOBJ_TYPECLASS = "worldloader.objects.AutoObj"
