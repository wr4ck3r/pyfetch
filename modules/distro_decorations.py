from re import S
from sty import fg, bg, ef, rs

colors = {"fr": fg.rs, "br": bg.rs, "eb": ef.bold, "rb": rs.bold_dim}

distros = {
    "arch": {
        "logo": r"""    _
   / \   CPU
  /   \   RAM
 /  _  \   Resolution
/_-' '-_\   Uptime
      OS
""",
        "colors": [
            fg(96, 154, 247), #pcolor
            fg(211, 223, 245), #vcolor
            fg(144, 181, 240), #logo color
        ],
    },
    "gentoo": {
        "logo": r"""  _----_  OS
(      \\  CPU
\\   0   \\  RAM
 \\       )  Resolution
 /     _/  Uptime
 \\___-""",
        "colors": [
            fg(159, 132, 240),
            fg(200, 190, 230),
            fg(84, 72, 122),
        ]
    },
    "linuxmint": {
        "logo": r"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   OS
▀▀█  █        █   CPU
  █  █  █  █  █   RAM
  █  █  █  █  █   Resolution
  █  ▀▀▀▀▀▀▀  █   Uptime
  ▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
        "colors": [
            fg(91, 237, 83),
            fg(222, 242, 220),
            fg(110, 230, 103),
        ],
    },
    "other": {
        "logo": r"""   .--.
   |o_o |
   |:_/ |  CPU
  //   \ \  RAM
 (|     | )  Resolution
/'\_   _/`\  Uptime
\___)=(___/
  OS""",
"colors": (
            fg(204, 241, 255),
            fg(247, 251, 252),
            fg(209, 246, 255),
        ),
    },
}
