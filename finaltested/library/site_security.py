#!/usr/bin/python
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}
from ansible.module_utils.basic import AnsibleModule
import requests,json
def incapsula():
    module_args = dict(
        api_id=dict(type='str', required=True),
        api_key=dict(type='str', required=True),
        site_id=dict(type='str', required=True),
        rule_id=dict(type='str', required=True),
        ips=dict(type='str', required=True)
    )
    url="https://my.incapsula.com/api/prov/v1/sites/configure/acl"
    result = dict(
        changed=False,
        original_message='',
        message1='',
        message2='',
        status_code=''
    )
    payload=dict(
          api_id='',
          api_key='',
          site_id='',
          rule_id='',
          ips=''
                )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        return result
    result['original_message'] = module.params['api_id']
    result['message1'] = module.params['rule_id']
    payload['api_id']=module.params['api_id']
    payload['api_key']=module.params['api_key']
    payload['site_id']=module.params['site_id']
    payload['rule_id']=module.params['rule_id']
    payload['ips']=module.params['ips']
    if module.params['api_id']:
       if module.params['api_id'] == 'fail me':
          result['changed'] = False
          module.fail_json(msg='You requested this to fail', **result)
       else:
          r=requests.post(url,data=payload)
          result['message2'] = r.json()
          result['status_code']=r.status_code
          result['changed'] = True
          module.exit_json(**result)
def main():
    incapsula()
if __name__ == '__main__':
    main()

