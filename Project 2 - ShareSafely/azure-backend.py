from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Initialize Azure Key Vault client
key_vault_url = "https://your-keyvault.vault.azure.net/"
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Get secrets from Key Vault
def get_secret(secret_name):
    try:
        return secret_client.get_secret(secret_name).value
    except Exception as e:
        print(f"Error retrieving secret {secret_name}: {str(e)}")
        return None

# Initialize Azure Storage settings
storage_account_name = get_secret("storage-account-name")
storage_account_key = get_secret("storage-account-key")
container_name = "uploads"

blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account_name}.blob.core.windows.net",
    credential=storage_account_key
)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Create a unique blob name
        blob_name = f"{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
        
        # Get container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Upload the file
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file.read())

        # Generate SAS token for the blob (24 hour access)
        sas_token = generate_blob_sas(
            account_name=storage_account_name,
            container_name=container_name,
            blob_name=blob_name,
            account_key=storage_account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=24)
        )

        # Generate the full URL with SAS token
        blob_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"

        return jsonify({
            'message': 'File uploaded successfully',
            'shareLink': blob_url
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
