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
            fg(96, 154, 247),
            fg(211, 223, 245),
            fg(144, 181, 240),
            bg(80, 145, 250),
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
            bg(125, 245, 113),
        ],
    },
}
