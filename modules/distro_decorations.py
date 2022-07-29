from re import S
from sty import fg, bg, ef, rs

colors = {"fr": fg.rs, "br": bg.rs, "eb": ef.bold, "rb": rs.bold_dim}

distros = {
    "arch": {
        "logo": r"""    _  CPU
   / \  RAM
  /   \  Resolution
 /  _  \  Uptime
/_-' '-_\  OS
      Kernel
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
 \\___-  Kernel""",
        "colors": [
            fg(159, 132, 240),
            fg(200, 190, 230),
            fg(84, 72, 122),
        ]
    },
    "ubuntu": {
        "logo": r"""   ,--(_)  OS
 _/ ;-._\  CPU
(_)(   ) )  RAM
  \ ;-'_/  Resolution
   `--(_)  Uptime
 Kernel""",
        "colors": (
                fg(242, 109, 63),
                fg(230, 180, 163),
                fg(233, 84, 32),
            )
    },
    "linuxmint": {
        "logo": r"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  OS
▀▀█  █        █  CPU
  █  █  █  █  █  RAM
  █  █  █  █  █  Resolution
  █  ▀▀▀▀▀▀▀  █  Uptime
  ▀▀▀▀▀▀▀▀▀▀▀▀▀  Kernel
""",
        "colors": (
            fg(91, 237, 83),
            fg(222, 242, 220),
            fg(110, 230, 103),
        ),
           },
    "other": {
        "logo": r"""    .--.  CPU
   |o_o |  RAM
   |:_/ |  Resolution
  //   \ \  Uptime
 (|     | )  Kernel
/'\_   _/`\  OS
\___)=(___/""",
"colors": (
            fg(204, 241, 255),
            fg(247, 251, 252),
            fg(209, 246, 255),
        ),
    },
}
