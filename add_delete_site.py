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
        site_id=dict(type='str', required=False),
        domain=dict(type='str', required=False),
        account_id=dict(type='str', required=False),
	state=dict(default='present', choices=['present', 'absent'])
        )
    addurl="https://my.incapsula.com/api/prov/v1/sites/add"
    deleteurl="https://my.incapsula.com/api/prov/v1/sites/delete"
    result = dict(
        changed=False,
        original_message='',
        message1='',
        message2='',
        status_code=''
        )
    addpayload=dict(
	  api_id='',
          api_key='',
          domain='',
          account_id=''
         )
    deletepayload=dict(
	api_id='',
	api_key='',
	site_id=''
	)
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
        )
    if module.check_mode:
        return result
    if module.params['state'] == 'present':
       result['original_message'] = module.params['api_id']
       result['message1'] = module.params['state']
       addpayload['api_id']=module.params['api_id']
       addpayload['api_key']=module.params['api_key']
       addpayload['domain']=module.params['domain']
       addpayload['account_id']=module.params['account_id']
       if module.params['api_id']:
          if module.params['api_id'] == 'fail me':
             result['changed'] = False
             module.fail_json(msg='You requested this to fail', **result)
          else:
            addresult=requests.post(addurl,data=addpayload)
            result['message2'] = addresult.json()
            result['status_code']=addresult.status_code
            result['changed'] = True
            module.exit_json(**result)
    if module.params['state'] == 'absent':
       result['original_message']=module.params['api_id']
       result['message1']=module.params['state']
       deletepayload['api_id']=module.params['api_id']
       deletepayload['api_key']=module.params['api_key']
       deletepayload['site_id']=module.params['site_id']
       if module.params['api_id']:
          if module.params['api_id'] == 'fail me':
             result['changed'] = False
             module.fail_json(msg='You requested this to fail', **result)
          else:
            deleteresult=requests.post(deleteurl,data=deletepayload)
            result['message2'] = deleteresult.json()
            result['status_code']=deleteresult.status_code
            result['changed'] = True
            module.exit_json(**result)			
def main():
    incapsula()
if __name__ == '__main__':
    main()

