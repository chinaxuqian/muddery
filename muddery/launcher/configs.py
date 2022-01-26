#!/usr/bin/env python
"""

"""

import os


MUDDERY_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MUDDERY_LIB = os.path.join(MUDDERY_ROOT, "muddery")
GAME_TEMPLATES = os.path.join(MUDDERY_LIB, "game_templates")

# Game directory structure
SETTING_FILE = "settings.py"
SERVER_DIR = "server"
CONF_DIR = os.path.join(SERVER_DIR, "conf")
SETTINGS_PATH = os.path.join(CONF_DIR, SETTING_FILE)
SETTINGS_DOTPATH = "server.conf.settings"
CURRENT_DIR = os.getcwd()
GAME_DIR = CURRENT_DIR
LOG_FILE = os.path.join(GAME_DIR, "server", "logs", "launcher.log")

DEFAULT_TEMPLATE = "default"

CONFIG_FILE = "game.cfg"
VERSION_SECTION = "VERSION"
VERSION_ITEM = "version"
TEMPLATE_ITEM = "template"


# ------------------------------------------------------------
#
# Messages
#
# ------------------------------------------------------------

CREATED_NEW_GAMEDIR = \
    """
    Welcome to Muddery!
    Created a new Muddery game directory '{gamedir}'.

    You can now optionally edit your new settings file
    at {settings_path}. If you don't, the defaults
    will work out of the box. When ready to continue, 'cd' to your
    game directory and run:

       muddery start

    This starts the server for the first time. Make sure to create
    a superuser when asked for it. You should now be able to (by
    default) connect to your server by pointing your web browser to
    http://localhost:{port}.
    """

CMDLINE_HELP = \
    """
    Starts or operates the Muddery game server. Also allows for
    initializing a new game directory and manages the game's database.
    You can also pass most standard django-admin arguments and
    options.
    """

VERSION_INFO = \
    """
    Muddery {version}
    OS: {os}
    Python: {python}
    Django: {django}
    {about}
    """

ABOUT_INFO = \
    """
    Muddery text game development system

    Licence: BSD 3-Clause Licence
    Web: http://www.muddery.org
    Forum: http://www.muddery.org/forum
    Maintainer (2015-):   Lu Yijun

    Use -h for command line options.
    """

ERROR_INPUT = \
    """
    Command
    {args} {kwargs}
    raised an error: '{traceback}'.
    """

ERROR_NO_GAMEDIR = \
    """
    You must run this command inside a valid game directory first
    created with

        muddery --init mygamename
    """

NEED_UPGRADE = \
    """
    Your game's version is too old. Please run:

        muddery --upgrade

    to upgrade your game.
    """

SERVER_INFO = \
    """{servername} Server {version}
    {status}
    """

ARG_OPTIONS = \
    """Actions on installed server. One of:
 start   - launch server+portal if not running
 reload  - restart server in 'reload' mode
 stop    - shutdown server+portal
 reboot  - shutdown server+portal, then start again
 reset   - restart server in 'shutdown' mode
 istart  - start server in foreground (until reload)
 ipstart - start portal in foreground
 sstop   - stop only server
 kill    - send kill signal to portal+server (force)
 skill   - send kill signal only to server
 status  - show server and portal run state
 info    - show server and portal port info
 menu    - show a menu of options
Others, like migrate, test and shell is passed on to Django."""