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
    "mint": {
        "logo": r"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   CPU
▀▀█  █        █   RAM
  █  █  █  █  █   Resolution
  █  █  █  █  █   Uptime
  █  ▀▀▀▀▀▀▀  █   OS
  ▀▀▀▀▀▀▀▀▀▀▀▀▀
""",
        "colors": [
            fg(91, 237, 83),
            fg(222, 242, 220),
            fg(110, 230, 103),
        ],
    },
    "other": {
        "logo": r"""    .--.   CPU
   |o_o |   RAM
   |:_/ |   Resolution
  //   \ \   Uptime
 (|     | )   OS
/'\_   _/`\
\___)=(___/""",
        "colors": (
            fg(204, 241, 255),
            fg(247, 251, 252),
            fg(209, 246, 255)
        ),
    }
}
