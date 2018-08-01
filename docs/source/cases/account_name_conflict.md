"""
# Account name conflict

<normal><pre>
This file can be executed as a python script: 
``python3 account_name_conflict.md``.

The set-up statements are explained in the <a href="setup.html">elsewhere</a>.
</pre></normal>

## Set-up
<normal><pre>
"""
import setup
import eosf
from eosf_wallet import Wallet
from eosf_account import account_create, account_master_create

eosf.set_throw_error(True)
eosf.reset([eosf.Verbosity.TRACE]) 
wallet = Wallet()
account_master_create("account_master")
eosf.set_throw_error(False)
"""
</pre></normal>
## Case
<normal><pre>
The ``EOSFactory`` wraps EOSIO accounts with objects. The symbolic name of an 
account object, for example ``account_alice``, has to be unique in a program. 
Moreover, it has be unique in a collection of scripts, especially, if they 
execute real transactions.

The ``EOSFactory`` uses mapping files that keep the uniqueness.

However, what if a user wants to ascribe a previously used name to another 
physical account. Then, the only way to keep the previous physical account 
within the system is to change its mapping name.

Create two account objects: ``account_alice`` and ``account_carrol``.

Then try to create another account object called ``account_alice``. Although
this object is going to refer to a new blockchain account, it cannot accept
the given name: error is issued.

You are prompted to change the blocking name. On acceptance, the ``nano`` 
editor opens. CTR+X, to save and exit.

Change ``account_alice`` to ``account_alice_b``.
</pre></normal>

<normal><pre>
"""
account_create("account_alice", account_master)
account_create("account_carrol", account_master)
account_create("account_alice", account_master)
"""
</pre></normal>

### Test run
<normal><pre>
In an linux bash, change directory to where this file exists, it is the 
directory ``docs/source/cases`` in the repository, and enter the following 
command:
</pre></normal>
<normal><pre>
$ python3 account_name_conflict.md
</pre></normal>
<normal><pre>
We hope that you get something similar to this shown in the image below.
</pre></normal>
<img src="account_name_conflict.png" 
    onerror="this.src='../../../source/cases/account_name_conflict.png'"   
    alt="account name conflict" width="640px"/>

"""
    /mnt/c/Workspaces/EOS/eosfactory/build/daemon/data-dir/wallet/accounts.json
* The account object is created.