class InvalidProjectToken(Exception):
    pass

class MissingProjectToken(Exception):
    pass

class MissingProjectRoot(Exception):
    pass

HELP_MESSAGE = """
  * To get client tokens, run `supso update`.

  * If you do not have the supso command line interface yet, first run `gem install supso`.

  * Visit http://supso.org/help for further help.
"""
