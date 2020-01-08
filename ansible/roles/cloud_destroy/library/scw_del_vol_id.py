#!/usr/bin/env python

from ansible.module_utils.scaleway import SCALEWAY_LOCATION, scaleway_argument_spec, Scaleway
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

def core(module):
    id_ = module.params['id']

    account_api = Scaleway(module)

    if module.check_mode:
        module.exit_json(changed=True)

    response = account_api.delete('/volumes/' + id_)
    if response.status_code == 204:
        module.exit_json(changed=True, data=response.json)
    elif response.status_code == 404:
        module.exit_json(changed=False)

    module.fail_json(msg='Error deleting volume [{0}: {1}]'.format(
        response.status_code, response.json))

def main():
    argument_spec = scaleway_argument_spec()
    argument_spec.update(dict(
        id=dict(required=True),
        region=dict(required=True, choices=SCALEWAY_LOCATION.keys()),
    ))
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    core(module)

if __name__ == '__main__':
    main()
