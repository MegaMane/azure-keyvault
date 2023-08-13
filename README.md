# azure-keyvault
Working With Azure Key Vault In Python Using a Service Principal

1. Create  a key vault
2. Create an App Registration in Azure Active Directory
3. Generate a secret for your App Registration
4. Note the value for your client secret and save it in your .env file
5. Note the value on the overview page for your app:  
   Application (client) ID  
   Directory (tenant) ID
6. Click on Subcrptions in the Azure portal and note the   
   Subscription ID
7. Back in the key vault click on Access policies click on create
8. Select the permissions Get and List for reading secrets, and Set and Delete if you want your service principal to be able to do that
9. After Clicking Next Type the name of your app registration (aka service principal) and add it.
10. In your .env file add the following key value pairs

KEY_VAULT_NAME="<Your Key Vault Name>"  
AZURE_CLIENT_ID="<Your Appliction (client) ID>"  
AZURE_CLIENT_SECRET="<Your Client Secret From Step 4>"  
AZURE_SUBSCRIPTION_ID="<Your Azure Subscription>"  
AZURE_TENANT_ID="<Your Azure Tenant>"  


References
------------

https://medium.com/@tophamcherie/using-environment-variables-in-python-66e9ca50f146

https://medium.com/@tophamcherie/authenticating-connecting-to-azure-key-vault-or-resources-programmatically-2e1936618789

https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli

https://note.nkmk.me/en/python-pip-install-requirements/
