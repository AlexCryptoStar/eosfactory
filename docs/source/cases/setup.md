"""
# Setting-up EOSFactory tests

<pre><normal>
This file can be executed as a python script: ``python3 setup.md``.
</pre></normal>

## Set-up part

### Throw exceptions status

<pre><normal>
The set-up part of a test does not involve testing specific assumptions.
Instead, the `EOSFactory` is set then to throw fatal exceptions: the set-up
block is enclosed within the following statements:
</pre></normal>

<pre><normal>
eosf.set_throw_error(True)
#
# set-up statements
#
eosf.set_throw_error(False)
</pre></normal>

### Verbosity status

<pre><normal>
You can determine the amount of the verbosity of the tested processes.
The output of the commands is made with objects of the `eosf.Logger` class.

The verbosity can assume the following values:

    * eosf.Verbosity.TRACE      # only main tasks are marked
    * eosf.Verbosity.EOSF       # subtasks are noted
    * eosf.Verbosity.OUT        # command output is printed
    * eosf.Verbosity.DEBUG      # debugging info is printed

Default is [eosf.Verbosity.EOSF, eosf.Verbosity.OUT]
</pre></normal>

### Code excerpt

<pre><normal>
The following script demonstrates steering statements:
</pre></normal>

<pre><normal>
"""
import setup
import eosf
from eosf_wallet import Wallet
from eosf_account import account_create, account_master_create

eosf.set_verbosity([eosf.Verbosity.EOSF, eosf.Verbosity.OUT])
setup.set_command_line_mode(False) # print message sent to the cleos
eosf.set_is_testing_errors(False) # make the error mesages alarming

eosf.set_throw_error(True) # throw exception rather then print message
eosf.restart()
eosf.use_keosd(False) # nodeos vs keosd wallet management
eosf.reset([eosf.Verbosity.TRACE]) # start local testnode
wallet = Wallet() # create the singleton `Wallet` object
account_master_create("account_master") # create local testnode `eosio` account
eosf.set_throw_error(False) # print message rather then throw exception

eosf.set_is_testing_errors() # make the error mesages less alarming
"""
</pre></normal>
"""