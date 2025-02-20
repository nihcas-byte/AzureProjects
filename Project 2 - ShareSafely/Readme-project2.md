# ShareSafely Project Documentation

## Overview

ShareSafely is a web application that enables users to securely upload files to Azure Blob Storage. Upon uploading, the application generates a unique, time-limited link for sharing, ensuring that only authorized users can access the file within the specified duration.

## Prerequisites

Before setting up the ShareSafely application, ensure you have the following:

- An active [Azure subscription](https://azure.microsoft.com/free/).
- Administrative access to the Azure portal.
- Basic knowledge of web application development and Azure services.

## Azure Services Utilized

The ShareSafely application leverages the following Azure services:

- **Azure Blob Storage**: For storing uploaded files securely.
- **Azure Web Apps**: To host the web application.
- **Azure Key Vault**: To manage and secure sensitive information like storage account keys.

## Setup Steps

Follow these steps to set up the ShareSafely application in the Azure portal:

### 1. Create a Resource Group

1. **Navigate to Resource Groups**:
   - Log in to the [Azure portal](https://portal.azure.com/).
   - In the left-hand menu, select **Resource groups**.

2. **Create a New Resource Group**:
   - Click on **+ Create**.
   - Fill in the required details:
     - **Subscription**: Select your subscription.
     - **Resource group**: Enter a unique name (e.g., `ShareSafelyRG`).
     - **Region**: Choose a region close to your users.
   - Click **Review + create**, then **Create**.

*Placeholder for Screenshot: Resource Group Creation*

### 2. Set Up Azure Blob Storage

1. **Navigate to Storage Accounts**:
   - In the Azure portal, select **Storage accounts** from the left-hand menu.

2. **Create a New Storage Account**:
   - Click on **+ Create**.
   - Fill in the following details:
     - **Subscription**: Select your subscription.
     - **Resource group**: Choose the resource group created earlier (`ShareSafelyRG`).
     - **Storage account name**: Enter a unique name (e.g., `sharesafelystorage`).
     - **Region**: Same as your resource group.
     - **Performance**: Standard.
     - **Replication**: Locally-redundant storage (LRS).
   - Click **Review + create**, then **Create**.

3. **Create a Blob Container**:
   - After the storage account is deployed, navigate to it.
   - Under **Data storage**, select **Containers**.
   - Click on **+ Container**.
   - Enter a name (e.g., `uploads`) and set the **Public access level** to **Private**.
   - Click **Create**.

*Placeholder for Screenshot: Storage Account and Container Creation*

### 3. Deploy the Web Application

1. **Navigate to App Services**:
   - In the Azure portal, select **App Services**.

2. **Create a New Web App**:
   - Click on **+ Create**.
   - Fill in the following details:
     - **Subscription**: Select your subscription.
     - **Resource group**: Choose `ShareSafelyRG`.
     - **Name**: Enter a unique name (e.g., `ShareSafelyApp`).
     - **Publish**: Code.
     - **Runtime stack**: Choose your application's runtime (e.g., .NET, Node.js).
     - **Region**: Same as your resource group.
   - Click **Review + create**, then **Create**.

3. **Deploy Application Code**:
   - Once the web app is created, navigate to it.
   - In the left-hand menu, select **Deployment Center**.
   - Choose your deployment source (e.g., GitHub, local Git) and follow the prompts to deploy your code.

*Placeholder for Screenshot: Web App Deployment*

### 4. Configure Azure Key Vault

1. **Navigate to Key Vaults**:
   - In the Azure portal, select **Key Vaults**.

2. **Create a New Key Vault**:
   - Click on **+ Create**.
   - Fill in the following details:
     - **Subscription**: Select your subscription.
     - **Resource group**: Choose `ShareSafelyRG`.
     - **Key vault name**: Enter a unique name (e.g., `ShareSafelyKV`).
     - **Region**: Same as your resource group.
   - Click **Review + create**, then **Create**.

3. **Add Secrets to Key Vault**:
   - After the Key Vault is created, navigate to it.
   - Under **Settings**, select **Secrets**.
   - Click on **+ Generate/Import**.
   - Enter the **Name** (e.g., `StorageAccountKey`) and the **Value** (your storage account key).
   - Click **Create**.

*Placeholder for Screenshot: Key Vault and Secret Creation*

### 5. Integrate Key Vault with Web App

1. **Assign Managed Identity to Web App**:
   - Navigate to your web app (`ShareSafelyApp`).
   - Under **Settings**, select **Identity**.
   - Set **Status** to **On** and click **Save**.

2. **Grant Access to Key Vault**:
   - Navigate back to your Key Vault (`ShareSafelyKV`).
   - Under **Access policies**, click on **+ Add Access Policy**.
   - Configure the following:
     - **Secret permissions**: Get.
     - **Select principal**: Search and select your web app's managed identity.
   - Click **Add**, then **Save**.

*Placeholder for Screenshot: Managed Identity and Access Policy Configuration*

### 6. Configure Application Settings

1. **Set Environment Variables**:
   - Navigate to your web app (`ShareSafelyApp`).
   - Under **Settings**, select **Configuration**.
   - Click on **+ New application setting** and add the following:
     - **Name**: `BlobStorageConnectionString`
     - **Value**: The connection string to your Blob Storage (retrieve it from the storage account's **Access keys** section).
   - Click **OK**, then **Save**.

*Placeholder for Screenshot: Application Settings Configuration*

### 7. Implement File Upload and Link Generation

1. **Develop Upload Functionality**:
   - In your application code, use Azure Storage SDKs to handle file uploads to the Blob Storage container (`uploads`).

2. **Generate Time-Limited Access Links**:
   - Implement functionality to create Shared Access Signatures (SAS) for uploaded files, setting expiration times as needed.

*Placeholder for Screenshot: Code Snippet for SAS Generation*

### 8. Monitor and Maintain

1. **Set Up Monitoring**:
   - Navigate to your web app (`ShareSafelyApp`).
   - Under **Monitoring**, select **Logs** and set up **Application Insights** for real-time monitoring.

2. **Implement Cleanup Mechanism**:
   - Use Azure Functions or Logic Apps to periodically delete expired files from the Blob Storage to manage storage costs and maintain security.

*Placeholder for Screenshot: Monitoring and Cleanup Configuration*

## Conclusion

By following these steps, you can successfully deploy the ShareSafely application, providing users with a secure platform to upload and share files with time-limited 
