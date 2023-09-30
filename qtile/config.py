from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from themes import Dracula, Midnight, Monokai, Tomorrow, One_dark, Nordic, Catppuccin, Custom

from keyBinding import bindings, mod

from qtile_extras import widget
from qtile_extras.widget import WiFiIcon, UPowerWidget, ALSAWidget
from qtile_extras.widget.decorations import PowerLineDecoration

import os
from datetime import datetime

theme =Custom

# Keybindings
keys = bindings


groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )



layouts = [
    layout.MonadTall(
        border_focus=theme["magenta"],
        border_width=2),
    layout.Max(),
]



widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=4,
    border_color= theme["blue"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox("•", foreground=theme["BG1"]),
                widget.TextBox("•", foreground=theme["BG1"]),

                # Time
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.Clock(format="%I:%M %p"),

                widget.Spacer(),

                widget.GroupBox(
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


 #: Wifi
                WiFiIcon(interface='wlp4s0',padding_x=10,padding_y=10,
                active_colour=theme["green"],inactive_colour=theme['BG1']),
                widget.TextBox("|", foreground=theme["BG1"]),

#: for brightness
                widget.TextBox("󰃝", foreground=theme["blue"],padding=7),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl1/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl1/max_brightness",
                    foreground=theme["green"],
                    scroll=True,
                    ),
#: for audio
                widget.TextBox("|", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                # widget.ALSAWidget(),
                widget.PulseVolume(foreground=theme["green"]),
                widget.TextBox("|", foreground=theme["BG1"]),

# cpu 
                widget.TextBox("",foreground=theme["blue"],padding=7 ),
                widget.CPU(format='{load_percent}%'),
                widget.TextBox("•", foreground=theme["BG1"]),

# cpu temp
                widget.ThermalSensor(),
                widget.TextBox("|", foreground=theme["BG1"]),

# battery
                #widget.UPowerWidget(),
                widget.TextBox("",foreground=theme["blue"],padding=9),
                widget.Battery(discharge_char='',format='{percent:1.0%}'),
                widget.TextBox("|", foreground=theme["BG1"]),

#: Check Updates               
                # widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.CheckUpdates(display_format='  {updates}',distro='Arch_yay',foreground=theme["blue"]),
                widget.TextBox("•", foreground=theme["BG1"]),
            ],
            30,
            background=theme['background'],
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
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"), 
        Match(wm_class="makebranch"),  
        Match(wm_class="maketag"),  
        Match(wm_class="ssh-askpass"), 
        Match(title="branchdialog"),  
        Match(title="pinentry"),  
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
