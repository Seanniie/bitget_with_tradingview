import pickle
import pandas as pd

name_1 = 'Seannie'
api_key_1 = 'write your api_key_1'
secret_key_1= 'write your secret_key_1'
passphrase_1= 'write your passphrase'

name_2 = 'account2'
api_key_2 = 'write your friend api_key2'
secret_key_2 = 'write your friend secret_key2'
passphrase_2 = 'write your friend passphrase'

name_3 = 'account3'
api_key_3 = 'write your friend api_key3'
secret_key_3 = 'write your friend secret_key3'
passphrase_3 = 'write your friend passphrase'

name_4 = 'account4'
api_key_4 = ''
secret_key_4 = ''
passphrase_4 = ''

name_5 = 'account5'
api_key_5 = ''
secret_key_5 = ''
passphrase_5 = ''

userInfoList = pd.DataFrame({
    'name':[name_1,name_2,name_3,name_4,name_5],
    'api_key':[api_key_1,api_key_2,api_key_3,api_key_4,api_key_5],
    'secret_key':[secret_key_1,secret_key_2,secret_key_3,secret_key_4,secret_key_5],
    'passphrase':[passphrase_1,passphrase_2,passphrase_3,passphrase_4,passphrase_5]
    })
userInfoList.to_pickle("userInfoList.pkl")