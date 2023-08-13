import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,ClientSecretCredential
from dotenv import load_dotenv

load_dotenv()

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{keyVaultName}.vault.azure.net"
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET')
tenant_id = os.getenv('AZURE_TENANT_ID')
secretName = 'sec-test-retrieve-secret'

credentials = ClientSecretCredential(client_id=client_id, client_secret=client_secret,tenant_id=tenant_id) 
client = SecretClient(vault_url = KVUri, credential = credentials)

retrieved_secret = client.get_secret(secretName)
print(retrieved_secret.value)