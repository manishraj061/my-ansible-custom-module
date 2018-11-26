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
        account_id=dict(type='str', required=True)
    )
    #url="http://httpbin.org/post"
    url="https://my.incapsula.com/api/prov/v1/sites/lp/users"
    #r=requests.post(url,data=module_args)   
    result = dict(
        changed=False,
        original_message='',
        message1='',
        message2='',
        status_code=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        return result
    result['original_message'] = module.params['api_id']
    #result['message1'] = r.json()['form']['key1']
    result['message1'] = module.params['account_id']
    #result['message2'] = r.json()
    #result['status_code']=r.status_code
    if module.params['api_id']:
       if module.params['api_id'] == 'fail me':
          result['changed'] = False
          module.fail_json(msg='You requested this to fail', **result)
       else:
          r=requests.post(url,data=module_args)
          result['message2'] = r.url
          result['status_code']=r.status_code
          result['changed'] = True
          module.exit_json(**result)
def main():
    incapsula()
if __name__ == '__main__':
    main()

