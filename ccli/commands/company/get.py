"""
ccli/commands/company/get.py

This file contains the source for the CLI command to get a ConnectWise company by id.
"""
from __future__ import (print_function, absolute_import)

import click
import suds

from blessings import Terminal

from ccli.lib.connectwise import ConnectwiseCompanyApi


####################################################################################################
# CLI Command "get" for group "company"

@click.command()
@click.option('--summary', is_flag=True, default=False, help='Show a summarized object.')
@click.argument('company_id')
def get(summary, company_id):
    """
    Get a company from the ConnectWise API via the company's record ID.

    :param summary:    Show a summary?
    :param company_id: ConnectWise company record ID.

    :return:
    """

    # Initialize the company api
    api = ConnectwiseCompanyApi()

    # Make the request
    try:
        company = api.get_company(company_id)
    except suds.WebFault as e:
        term = Terminal()
        if 'First error message' in e.message:
            e.message = e.message.split('First error message: ')[1][:-1]
        print('{t.bright_red}{e.message}{t.normal}'.format(t=term, e=e))
        exit()

    # Show the data
    if summary:
        from terminaltables import SingleTable
        table = SingleTable([
            ('ID', 'Company Name'),
            (company.Id, company.CompanyName)], ' Summary ')
        table.justify_columns[0] = 'right'
        print(table.table)
        return
    else:
        print(company)
        return
