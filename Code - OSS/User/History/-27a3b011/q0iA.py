# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from themes import Dracula, Midnight, Monokai, Tomorrow, One_dark, Nordic, Catppuccin

from qtile_extras import widget
from qtile_extras.widget import WiFiIcon
from qtile_extras.widget.decorations import PowerLineDecoration
# from qtile_extras.widget.decorations import BrightnessControl



mod = "mod4"
terminal = guess_terminal()
# theme = Dracula
# theme = Midnight
# theme = Monokai
# theme = Tomorrow
# theme = One_dark
theme = Nordic
# theme = Catppuccin

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod,"shift"], "w", lazy.spawn('brave'), desc="Launch Browser"),
    Key([mod,"shift"], "f", lazy.spawn('thunar'), desc="Launch File Browser"),
    Key([mod,"shift"], "c", lazy.spawn('slack'), desc="Launch Chat app"),
    Key([mod,"shift"], "n", lazy.spawn('obsidian'), desc="Launch Chat app"),

    # Lunch rofi for different things
    Key([mod], "Tab", lazy.spawn('rofi -show window -show-icons'), desc="Launch Rofi to toggle between windows"),
    Key([mod],"r", lazy.spawn('rofi -show drun -show-icons'), desc="Launch window"),
    Key([mod],"x", lazy.spawn('rofi -show p -modi p:"rofi-power-menu" -font "JetBrains Mono NF 16"'), desc="Launch window"),

    # Toggle between different layouts as defined below
    Key([mod], "l", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        border_focus=theme["blue"],
        border_width=2),
    layout.Max(),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=4,
    border_color= theme["cyan"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayoutIcon(scale=.6),
                # widget.CurrentLayout(),
                # widget.TextBox("•", foreground=theme["BG1"]),
                
                # Date

                widget.TextBox("•", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.Clock(format="%Y-%m-%d %a"),
                widget.TextBox("•", foreground=theme["BG1"]),

                # Time
                # widget.TextBox("TIME:", foreground=theme["BG6"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.Clock(format="%I:%M %p"),

                widget.Spacer(),

                widget.GroupBox(
                    # highlight_method='line',
                    highlight_method='text',
                    foreground=theme["foreground"],
                    active = theme["white"],
                    inactive = theme["BG6"],
                    this_current_screen_border= theme["yellow"],
                    urgent_border = theme["red"],
                    urgent_text = theme["red"],
                    padding_x = 8
                    
                    ),

                widget.Spacer(),

                # widget.TextBox("•", foreground=theme["BG1"]),

                # widget.Prompt(),                
                # widget.WindowName(),
                # widget.WindowName(foreground=theme["blue"]),

                widget.Pomodoro(
                    color_inactive=theme["red"],
                    color_active=theme["green"],
                    color_break=theme["yellow"] ),
                widget.TextBox("•", foreground=theme["BG1"]),

                # Add clipboard icon
                # widget.Clipboard(),
                # widget.TextBox("•", foreground=theme["BG1"]),

# for brightness
                widget.TextBox("󰃝", foreground=theme["blue"],padding=7),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl1/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl1/max_brightness",
                    foreground=theme["green"],
                    scroll=True,
                    ),
                widget.TextBox("•", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.PulseVolume(foreground=theme["green"]),
                widget.TextBox("•", foreground=theme["BG1"]),


                widget.CPU(format=' {load_percent}%'),
                widget.TextBox("•", foreground=theme["BG1"]),
                # Add thurmometer icon

                widget.TextBox("",foreground=theme["blue"]),
                widget.ThermalSensor(),
                widget.TextBox("•", foreground=theme["BG1"]),

# battery
                widget.TextBox("",foreground=theme["blue"],padding=10),
                widget.Battery(discharge_char='',format='{char}{percent:2.0%}'),
                widget.TextBox("•", foreground=theme["BG1"]),

                # Probably not needed

                # WiFiIcon(),

                # Needed but doesn't work
                # widget.Wlan(),
                # widget.TextBox("•", foreground=theme["BG1"]),


                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead

                # widget.StatusNotifier(),

                # widget.TextBox(" "),
                # widget.QuickExit(),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background=theme['background'],
            # padding=10
            
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
