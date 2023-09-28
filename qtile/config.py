from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from themes import Dracula, Midnight, Monokai, Tomorrow, One_dark, Nordic, Catppuccin, Custom
from qtile_extras import widget
from qtile_extras.widget import WiFiIcon
from qtile_extras.widget.decorations import PowerLineDecoration

import os
from datetime import datetime



mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()
theme = Custom
#: Set your desired screenshots directory
screenshot_dir = "/home/abhi/Screenshots/" 



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod1], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
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
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    #: Toggle between split and unsplit sides of stack.
    #: Split = all windows displayed
    #: Unsplit = 1 window displayed, like Max layout, but still with
    #: multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),

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
    
    # Take screenshot
    # Take a whole-screen screenshot with Win + PrtSc
    Key([mod], "Print",
        lazy.function(lambda qtile: qtile.cmd_spawn(f"maim {screenshot_dir}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"))
    ),

    # Take a screenshot of a selected area with Win + Shift + S
    Key([mod, "shift"], "s",
        lazy.function(lambda qtile: qtile.cmd_spawn(f"maim -s {screenshot_dir}/selected_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"))
    ),
]

groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend(
        [
            #: mod1 + letter of group = switch to group
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
        border_focus=theme["blue"],
        border_width=2),
    layout.Max(),
]



widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    padding=4,
    border_color= theme["blue"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox("•", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.Clock(format="%Y-%m-%d %a"),
                widget.TextBox("•", foreground=theme["BG1"]),

                # Time
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.Clock(format="%I:%M %p"),

widget.TextBox("•", foreground=theme["BG1"]),
widget.TextBox("󰍡",foreground=theme["blue"]),
widget.Notify(),

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

                # widget.Pomodoro(
                #     color_inactive=theme["red"],
                #     color_active=theme["green"],
                #     color_break=theme["yellow"] ),
                # widget.TextBox("|", foreground=theme["BG1"]),

# for brightness
                widget.TextBox("󰃝", foreground=theme["blue"],padding=7),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl1/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl1/max_brightness",
                    foreground=theme["green"],
                    scroll=True,
                    ),
                widget.TextBox("|", foreground=theme["BG1"]),
                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.PulseVolume(foreground=theme["green"]),
                widget.TextBox("|", foreground=theme["BG1"]),

           # WiFiIcon(),

                

# cpu 
                widget.TextBox("",foreground=theme["blue"],padding=7 ),
                widget.CPU(format='{load_percent}%'),
                widget.TextBox("•", foreground=theme["BG1"]),
# cpu temp
                widget.ThermalSensor(),
                widget.TextBox("|", foreground=theme["BG1"]),
# gpu temp
                widget.TextBox("󰘚",foreground=theme["blue"]),
                widget.NvidiaSensors(),
                widget.TextBox("|", foreground=theme["BG1"]),
# Check Updates               

                widget.TextBox("",foreground=theme["blue"],padding=7),
                widget.CheckUpdates(display_format='{updates}'),
                widget.TextBox("|", foreground=theme["BG1"]),
                
# battery
                widget.TextBox("",foreground=theme["blue"],padding=10),
                widget.Battery(discharge_char='',format='{percent:1.0%}'),
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
