
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from settings.keys import *

groups = [Group(i) for i in [

    "   ", "   ", " 󰨞  ", " 󰙯  ", "   ", "   ", "   ", " 󰈙  ", "   ",
]]

for i, group in enumerate(groups):
    workSpaces = str(i+1)
    keys.extend(
        [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    workSpaces,
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    workSpaces,
                    lazy.window.togroup(group.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(group.name),
                ),
            ]
    )
