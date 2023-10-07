from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from themes import Dracula, Midnight, Monokai, Tomorrow, One_dark, Nordic, Catppuccin, Custom

from keyBinding import bindings, mod

from qtile_extras.widget import WiFiIcon
from widgets.battery_text import BatteryText


import os
from datetime import datetime

# theme to choose
# theme = Custom
theme =Custom

# Keybindings
keys = bindings


groups = [Group(i) for i in "1234567"]

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
        #border_focus=theme["BG1"],
        border_focus="00000033",
        border_width=0,
        margin=6,
        ),

    layout.Max(),
]



widget_defaults = dict(
    font="JetBrains Mono Nerd",
    fontsize=14,
    padding=4,
    border_color= theme["blue"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.TextBox("•", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["magenta"],padding=7),
                widget.Clock(format="%Y-%m-%d %a"),
                widget.TextBox("|", foreground=theme["BG1"]),

                # Time
                widget.TextBox("",foreground=theme["magenta"],padding=7),
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
                    padding_x = 14
                    
                    ),

                widget.Spacer(),
               # widget.Memory(),
                 #: Wifi
                WiFiIcon(interface='wlp4s0',padding_x=8,padding_y=8,
                active_colour=theme["magenta"],inactive_colour=theme['BG1']),
                widget.TextBox("|", foreground=theme["BG1"]),

#: for audio
                widget.TextBox("",foreground=theme["magenta"],padding=7),
                widget.PulseVolume(foreground=theme["magenta"]),
                widget.TextBox("|", foreground=theme["BG1"]),
                #widget.Volume(channel='IEC958'),

#: for brightness
                widget.TextBox("󰃝", foreground=theme["magenta"],padding=7),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl1/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl1/max_brightness",
                    ),
                widget.TextBox("|", foreground=theme["BG1"]),
# cpu 
                widget.TextBox("",padding=7 ),
                widget.CPU(format='{load_percent}%'),
                widget.TextBox("•", foreground=theme["BG1"]),

# cpu temp
                widget.ThermalSensor(),
                widget.TextBox("|", foreground=theme["BG1"]),

BatteryText(
                    10,
                    foreground=theme["foreground"],
                    fontsize=14,
                ),
#: Check Updates
                # widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.CheckUpdates(display_format='  {updates}',distro='Arch_yay',foreground=theme["yellow"]),
                widget.TextBox("•", foreground=theme["BG1"]),
            ],
            30,
            background="1f1d2ecc",
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
