"""
ccli/lib/connectwise/common.py

Common classes that will be used by all API modules in this module.
"""
import logging

from suds.client import Client

from ccli import ENVIRONMENT


####################################################################################################
# Setup Logging

logging.basicConfig(level=logging.ERROR, filename='suds.log')
logging.getLogger('suds.client').setLevel(logging.ERROR)


####################################################################################################
# Classes

class ConnectwiseApi(object):
    """
    Base class for creating a ConnectWise API.
    """

    def __init__(self, wsdl_name):
        """
        Constructor.

        :param wsdl_name: Name of the .wsdl file for this API.
        :type wsdl_name: str
        """
        # Initialize the suds client
        self.client = Client('{}v4_6_release/apis/2.0/{}?wsdl'.format(ENVIRONMENT.connectwise_site_url, wsdl_name))

        # Initialize the suds credentials object
        self.credentials = self.client.factory.create('ApiCredentials')
        self.credentials.CompanyId = ENVIRONMENT.connectwise_org_name
        self.credentials.IntegratorLoginId = ENVIRONMENT.connectwise_username
        self.credentials.IntegratorPassword = ENVIRONMENT.connectwise_password
