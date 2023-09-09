import os
import json

OIDC_Client = '0ac88307-b5dd-4035-9787-332a80e8f655' # your oidc connect client inum value
OIDC_Secret = '1234'  # your oidc connect client secret
Host = 'https://4x.gluu.org' # your host server name

#print(os.popen('curl -k '+Host+'/.well-known/openid-configuration'))

token_endpoint = Host + '/oxauth/restv1/token'
scim_endpoint = Host + '/identity/restv1/scim/v2/'
scim_users_endpoint = scim_endpoint + 'Users'
scim_groups_endpoint = scim_endpoint + 'Groups'
scim_fido_devices = scim_endpoint + 'FidoDevices'
scim_fido2_devices = scim_endpoint + 'Fido2Devices'

grant_type = 'client_credentials'

get_token_cmd = 'curl -k -u \'02c6aeda-e45a-40f3-af61-81967b0ddf3a:1234\' -d grant_type='+grant_type+ ' ' + token_endpoint
tt = os.popen(get_token_cmd).read()
res = json.loads(tt)
print(type(res))
print(res)
print(res['access_token'])
access_token = res['access_token']
token_type = res['token_type']
expires_in = res['expires_in']

get = 'curl -k -G -H "accept: application/scim+json" -H \'Authorization: Bearer '+access_token+ '\' '
users = get + scim_users_endpoint
groups = get + scim_groups_endpoint
fido_devices = get + scim_fido_devices
fido2_devices = get + scim_fido2_devices

res_users = json.loads(os.popen(users).read())
res_groups = json.loads(os.popen(groups).read())
res_fido_devices = json.loads(os.popen(fido_devices).read())
res_fido2_devices = json.loads(os.popen(fido2_devices).read())

with open("users.json", 'w') as file:
    json.dump(res_users, file)

with open("groups.json", 'w') as file:
    json.dump(res_groups, file)

with open("fido.json", 'w') as file:
    json.dump(res_fido_devices, file)

with open("fido2.json", 'w') as file:
    json.dump(res_fido2_devices, file)

