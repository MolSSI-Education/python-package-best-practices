"""

"""

import sphinx.highlighting

from typing import Any


class PygmentsBridgeExtended(sphinx.highlighting.PygmentsBridge):
    def get_lexer(
        self,
        source: str,
        lang: str,
        opts: dict | None = None,
        force: bool = False,
        location: Any = None,
    ) -> sphinx.highlighting.Lexer:
        
        split = lang.split(".")

        try:
            lang = split[1]
        except IndexError:
            pass

        return super().get_lexer(source, lang, opts, force, location)


sphinx.highlighting.PygmentsBridge = PygmentsBridgeExtended
