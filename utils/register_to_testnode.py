from  eosfactory import *
import argparse

def register(testnode_url, account_object_name):

    set_nodeos_address(testnode_url)

    if not eosf.node_is_operative():
        print(
            "This test needs the testnode {} running, but it does not answer." \
                .format(testnode_url))
        return

    create_wallet(file=True)
    create_master_account(account_object_name)

import argparse

parser = argparse.ArgumentParser(description='''
Given an url and the account object name, get registration data.
Apply the data to the registration form of the testnet.
Enter 'go' when ready.

Example:
    python3 register_to_testnode.py https://api.kylin-testnet.eospace.io account_master
''')
parser.add_argument("testnode_url")
parser.add_argument("account_object_name")

args = parser.parse_args()
register(args.testnode_url, args.account_object_name)
