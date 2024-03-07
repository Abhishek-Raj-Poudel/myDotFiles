from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from themes import Dracula, Midnight, Monokai, Tomorrow, One_dark, Nordic, Catppuccin, Custom, Monocrome, Gruvbox

from keyBinding import bindings, mod

from qtile_extras.widget import WiFiIcon
from widgets.battery_text import BatteryText


import os
from datetime import datetime

# theme to choose
# theme = Custom
theme = Gruvbox

# Keybindings
keys = bindings

groups = [
    Group("", matches=[Match(wm_class=['kitty'])]),
    Group("󰵅", matches=[Match(wm_class=['slack'])]),
    Group("󰾔", matches=[Match(wm_class=['brave-browser'])]),
    Group("󰅨", matches=[Match(wm_class=["code-oss"])]),
    Group("󱞁", matches=[Match(wm_class=["obsidian"])]),
    Group("󰎄", matches=[Match(wm_class=["spotify"])]),
    Group(""),
]
for i, group in enumerate(groups):
    keys.extend(
        [
            Key([mod], str(i + 1), lazy.group[group.name].toscreen(), desc=f"Switch to group {group.name}"),
            Key([mod, "shift"], str(i + 1), lazy.window.togroup(group.name), desc=f"Move focused window to group {group.name}"),
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
                #Date
                widget.TextBox("",padding=7,foreground=theme["foreground"] ),
                widget.Clock(format="%Y-%m-%d %a",foreground=theme["foreground"]),
                widget.TextBox("|", foreground=theme["BG1"]),
                # Time
                widget.Clock(format="%I:%M %p",foreground=theme["foreground"]),

                widget.Spacer(),

                widget.GroupBox(
                    highlight_method='text',
                    foreground=theme["yellow"],
                    active = theme["white"],
                    inactive = theme["BG3"],
                    this_current_screen_border= theme["green"],
                    urgent_border = theme["red"],
                    urgent_text = theme["red"],
                    padding_x = 12,
                    fontsize = 18
                ),

                widget.Spacer(),

                 #: Wifi
                WiFiIcon(interface='wlp4s0',padding_x=8,padding_y=8,
                inactive_colour=theme['BG1'], active_colour=theme["foreground"]),

                #: for audio
                widget.TextBox("",padding=7,foreground=theme["foreground"]),
                widget.PulseVolume(foreground=theme["foreground"]),
                widget.TextBox("|", foreground=theme["foreground"]),

                #: for brightness
                widget.TextBox("󰃝",padding=7, foreground=theme["foreground"]),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl1/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl1/max_brightness",
foreground=theme["foreground"]
                    ),
                widget.TextBox("|", foreground=theme["BG1"]),

                #: Battery widget
                BatteryText(
                    10,
                    foreground=theme["foreground"],
                    fontsize=14,
                ),
                #: Widgit Box like hamburger menu for the bar 
                widget.WidgetBox(widgets=[ 
                widget.TextBox("|", foreground=theme["BG1"]),
                # cpu 
                widget.CPU(format='   {load_percent}%',foreground=theme['foreground']),
                # Cpu Temp 
                widget.ThermalSensor(foreground=theme['foreground']),
                widget.TextBox("|", foreground=theme["BG1"]),
                widget.NvidiaSensors(fmt='󰘚   {}' ,foreground=theme['foreground']),
                widget.TextBox("|", foreground=theme["BG1"]),
                #: Check Updates
                widget.CheckUpdates(display_format='   {updates}',distro='Arch_yay',foreground=theme["yellow"]),
                ],
                text_open='󰅖',
                text_closed='󰍜',
                close_button_location='right',
                foreground=theme['foreground']
                ),
                widget.TextBox("•", foreground=theme["BG1"]),
            ],
            30,
            background='282828'
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
