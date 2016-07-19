"""
ccli/

This module contains the source code for the ConnectWise SOAP CLI.
"""


####################################################################################################
# Module Definitions

APP = 'ccli'
AUTHOR = 'Jacob A. Bridges'
VERSION = 'alpha'

from .lib.environment import AppRcParser
ENVIRONMENT = AppRcParser()

from blessings import Terminal
TERM = Terminal()
