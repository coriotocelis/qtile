
from libqtile import bar, widget
from libqtile.config import Screen
from settings.constans import *

widget_defaults = dict(
    font="Mononoki Nerd Font Complete Bold", # Ubuntu Mono Nerd Font
    fontsize=10,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # Left Site  ------------------------------------------------------

                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.ThermalSensor(background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("", background=COLOR_ONE , fontsize=SIZE_ONE_FIVE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.Memory(measure_mem='G', background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.Net(format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("󱚻 ", background=COLOR_ONE , fontsize=SIZE_ONE_FIVE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
            
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.CPU(format='{freq_current}GHz {load_percent}%', background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("󰍛", background=COLOR_ONE , fontsize="17", foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                # -----------------------------------------------------------------

                # Center Site -----------------------------------------------------
                
                widget.Spacer(),

                widget.TextBox("", foreground="#4c566a", fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.GroupBox(
                    inactive=COLOR_TWO,
                    active="#d8dee9",
                    highlight_method='line',
                    this_current_screen_border="#d8dee9",
                    fontsize=15,
                    padding=1,
                    background="#4c566a",
                    highlight_color=['4c566a', '4c566a']
                    ),
                widget.Prompt(),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("", foreground="#4c566a", fontsize=SIZE_TWO_TWO , padding=(-1)),

                # -----------------------------------------------------------------

                # Right Site -----------------------------------------------------

                widget.Spacer(),

                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.Systray(background=COLOR_ONE),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),

                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.TextBox("", background=COLOR_ONE , foreground=COLOR_TWO, fontsize="13"),
                widget.Clock(format="%d-%m-%y %a %I:%M %p", background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.TextBox("󰕾", background=COLOR_ONE , foreground=COLOR_TWO, fontsize=SIZE_ONE_FIVE),
                widget.Volume(fmt='{}', background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.CurrentLayout(background=COLOR_ONE , foreground=COLOR_TWO),
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                
                widget.TextBox("", foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),
                widget.TextBox(" 󰁹", background=COLOR_ONE , padding=(0), foreground=COLOR_TWO, fontsize="13"),
                widget.Battery(format='{percent:2.0%}', background=COLOR_ONE , foreground=COLOR_TWO), 
                widget.TextBox("",foreground=COLOR_ONE ,fontsize=SIZE_TWO_TWO , padding=(-1)),

                widget.QuickExit(default_text='', countdown_format='[{}]', foreground=COLOR_TWO, fontsize=SIZE_ONE_FIVE , padding=(5)),
                widget.TextBox(" "),

                # -----------------------------------------------------------------

            ],
            24,
            background = "#2e3440",
            border_width=[0, 0, 3, 0],
        ),
    ),
]
