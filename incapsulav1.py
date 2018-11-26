#!/usr/bin/python
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}
from ansible.module_utils.basic import AnsibleModule
import requests,json
def run_module():
    module_args = dict(
        key1=dict(type='str', required=True),
        key2=dict(type='str', required=True)
    )
    url="http://httpbin.org/post"
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
    result['original_message'] = module.params['key1']
    #result['message1'] = r.json()['form']['key1']
    result['message1'] = module.params['key1']
    #result['message2'] = r.json()
    #result['status_code']=r.status_code
    if module.params['key1']:
       if module.params['key1'] == 'fail me':
          result['changed'] = False
          module.fail_json(msg='You requested this to fail', **result)
       else:
          r=requests.post(url,data=module_args)
          result['message2'] = r.json()
          result['status_code']=r.status_code
          result['changed'] = True
          module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()

