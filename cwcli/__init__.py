"""
ccli/

This module contains the source code for the ConnectWise SOAP CLI.
"""
import os


# Load the application metadata
exec(open(os.path.dirname(os.path.realpath(__file__)) + '/meta.py', 'r').read())

####################################################################################################
# Module Definitions

APP = __app__

from cwcli.lib.environment import AppRcParser
ENVIRONMENT = AppRcParser()
