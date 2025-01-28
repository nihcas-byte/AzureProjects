### **Onboard Automator (Manage Entra ID identities and governance)**

Here’s a functional requirement derived from your steps:  
## **Functional Requirement: Automated Employee Onboarding in Azure AD**  


## Azure Logic App

Here’s a list of key Azure Logic Apps terms: 

1. **Logic App** – A cloud-based workflow automation service for integrating apps, data, and services.
2. **Workflow** – A sequence of steps defining automated Logic App processes.
3. **Trigger** – An event that starts a Logic App workflow (e.g., receiving an email or a timer schedule).
4. **Action** – A task or operation performed within a workflow, such as sending an email or updating a database.
5. **Connector** – A prebuilt integration component that allows Logic Apps to communicate with services like Office 365, SQL, and Azure Blob Storage.
    1. **Managed Connector** – A built-in or Microsoft-maintained connector requiring authentication to interact with external services.
    2. **Custom Connector** – A user-defined connector to integrate with third-party APIs not covered by built-in connectors.
6. **Built-in Actions** – Native actions available within Logic Apps without external authentication.
7. Plans:
    1. **Standard Plan** – A pricing model for hosting Logic Apps within Azure App Service with enhanced networking options.
    2. **Consumption Plan** – A pay-per-use pricing model where Logic Apps execute only when triggered.
    3. **Integration Service Environment (ISE)** – A dedicated environment for running Logic Apps with better security, scalability, and VNET integration.
    4. **Enterprise Integration Pack (EIP)** – A set of features that help integrate Logic Apps with legacy B2B protocols like AS2, X12, and EDIFACT.
8. **Stateful Workflow** – A workflow that maintains execution history and supports long-running operations.
9. **Stateless Workflow** – A lightweight workflow that executes quickly without persisting execution history.
10. **Run History** – A log of past executions, showing the status, inputs, and outputs of each Logic App run.
11. **Retry Policy** – A mechanism to automatically retry failed actions based on predefined settings.
12. **Parallel Execution** – A feature that allows multiple actions to run simultaneously within a Logic App.
13. Controls:
    1. **Loop** – A control flow construct (*For Each*, and *Until*) used to repeat actions within a Logic App.
    2. **Condition** – A logical statement that determines the execution path of a workflow.
14. **Expression** – A formula using functions and variables to manipulate data dynamically within Logic Apps.
15. **Variables** – Temporary storage for values that can be modified and used within a workflow.
16. **Secure Inputs/Outputs** – A setting to mask sensitive data within Logic App runs for security.
17. **API Connection** – A resource that stores authentication details for connectors like Office 365, Salesforce, and SharePoint.
18. **Message Queues** – Services like Azure Service Bus or Storage Queues used to process messages asynchronously.
19. **Monitoring & Alerts** – Tools like Azure Monitor and Application Insights to track Logic App performance and failures.

## Workflow flowchart:

![image](https://github.com/user-attachments/assets/fc2e85e4-830c-49b6-8a84-fb5ae91fd070)


## Creating a Logic App on Azure Portal:

Login to Azure Portal, navigate to Logic Apps and start with the creation of Logic App.

![image](https://github.com/user-attachments/assets/9648b6ea-1687-45ae-a6b6-9d1bbad077aa)


Logic App is created.

![image](https://github.com/user-attachments/assets/c14391e2-a061-4aeb-b7d7-a5c97fbd2c39)


Workflow is created under the ***Logic app designer.***

![image](https://github.com/user-attachments/assets/099690b2-c086-4b8d-acf6-0a8c68b43bdc)


## A New Line Item in the SharePoint List:

Adding a new Item in the list with User details (First Name, Last Name, Department, Location etc.). Note: that Department is IT hence, this account will become member of Security group called “*IT administrators*”

> **Note**: *Microsoft Lists* and *SharePoint Lists* are two different services. To work with Azure Logic App connecter we only have support for SharePoint Lists only.
> 

![image](https://github.com/user-attachments/assets/4a0146dd-0e55-4deb-bb6a-8bb6242dec49)


A new item is added to the SharePoint List.

![image](https://github.com/user-attachments/assets/ce3eb61e-440f-457d-adbd-8d5c80a72a67)
*Yes, I know the contact number is formatted with commas 😃

## Logic App trigger and Run on Azure Portal:

Let’s look at the Logic Apps Run History. The Logic App (**onboarder_LA**) run was successful. 
![image](https://github.com/user-attachments/assets/d8bf3ebd-a4cc-4e99-951a-16f50abe204d)



For a particular run under the Run History on Azure, we can check and validate if individual actions were successful/failed and their processing time. This Run History view and data enables to troubleshoot the Logic App flows easily.

![image](https://github.com/user-attachments/assets/662a1963-ab13-4ed3-ac70-5e9a2a277ae6)

For any failed action on any of the connectors, you get the below error message. The flow stops here and does not proceed further.

![image](https://github.com/user-attachments/assets/4a2d46c7-5864-436f-b53c-5b278bbd6222)


We can drill down and check individual steps to see their inputs and outputs. Below here it shows that when an item is created in SharePoint list then these values were captured. These will be used by downstream actions in the Logic App flow.

![image](https://github.com/user-attachments/assets/92f7f7eb-ee30-4bf6-b23f-7c3fa6a10fd0)

## Azure Portal User account creation:

Now, check on Azure Portal (portal.azure.com) for the user account creation.

![image](https://github.com/user-attachments/assets/561e5a7e-da85-4a0e-b152-fa701d339583)

User account has been created. 

![image](https://github.com/user-attachments/assets/9c5945cb-7a04-4b8f-bda3-dae1a80a7f46)


User Account details, this account is part of one security group called “*IT administrators*”

![image](https://github.com/user-attachments/assets/49987c49-f302-49fe-9504-e70f2df39ed1)

![image](https://github.com/user-attachments/assets/4dce486d-7562-4623-be33-ddf3277c0318)

Portals/Tools:

1. Azure Portal (*portal.azure.com*)
2. SharePoint Online (Lists)
3. Mailbox client and email account

Final Thoughts:
1. This project helped me understand Azure and Microsoft services such as Logic Apps and connectors, SharePoint Lists, Entra ID, Security groups and user accounts.
2. The project can reinforce the basics of IAM and automation of workflow.
