from libqtile.config import  Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
from datetime import datetime

mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()
screenshot_dir = "/home/abhi/pictures/screenshots" 

bindings = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod1], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
   # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows around
     # Move focus to the next screen
    Key([mod,"control"], "Right",lazy.screen.next_group(),desc="Move focus to the next screen"),
    # Move focus to the previous screen
    Key([mod,"control"], "Left",lazy.screen.prev_group(),desc="Move focus to the previous screen"),

    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Lunch software and codes
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod,"shift"], "w", lazy.spawn('brave'), desc="Launch Browser"),
    Key([mod,"shift"], "f", lazy.spawn('thunar'), desc="Launch File Browser"),
    Key([mod,"shift"], "c", lazy.spawn('slack'), desc="Launch Chat app"),
    Key([mod,"shift"], "n", lazy.spawn('obsidian'), desc="Launch Chat app"),
    Key([mod,"shift"], "p", lazy.spawn('code'), desc="Launch Chat app"),

    # Lunch rofi for different things
    Key([mod], "Tab", lazy.spawn('rofi -show window -show-icons'), desc="Launch Rofi to toggle between windows"),
    Key([mod],"r", lazy.spawn('rofi -show drun -show-icons'), desc="Launch window"),
    Key([mod],"x", lazy.spawn('rofi -show p -modi p:"rofi-power-menu" -font "JetBrains Mono NF 16"'), desc="Launch window"),

    # Toggle between different layouts as defined below
    Key([mod], "l", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
#grow and shrink layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # Take screenshot
    # Take a whole-screen screenshot with Win + PrtSc
    Key([mod], "Print",
        lazy.function(lambda qtile: qtile.cmd_spawn(f"maim {screenshot_dir}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"))
    ),

     #Take a screenshot of a selected area with Win + Shift + S
    Key([mod, "shift"], "s",
       lazy.function(lambda qtile: qtile.cmd_spawn(f"maim -s {screenshot_dir}/selected_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"))
    ),
]
