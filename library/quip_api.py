#!/usr/bin/env python2

import sys
import os

from ansible.module_utils import quip

def main():
    module = AnsibleModule(
        argument_spec = dict(
            access_token=dict(type='str', required=True),
            requests=dict(type='dict', required=True),
        ),
        supports_check_mode = False,
    )
    
    changed = True
    access_token = module.params['access_token']
    requests = module.params['requests']
    
    client = quip.QuipClient(access_token=access_token)
    
    results = []
    
    for name, args in requests.iteritems():
        method = getattr(client, name)
        results.append({
            'name': name,
            'args': args,
            'response': method(**args),
        })
            
    module.exit_json(
        changed = changed,
        results = results,
    )    

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.known_hosts import *

if __name__ == '__main__':
    main()