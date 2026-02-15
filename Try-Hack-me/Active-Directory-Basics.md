🧩 Core Components of a Windows Domain

The core of any Windows Domain is the Active Directory Domain Services (AD DS). This service acts as a central catalogue that holds the information of all "objects" within the network.

Among the many object types supported by Active Directory are:

    Users

    Machines

    Groups

    Printers

    Shares

    And more...

Let’s break down some of the core objects:
👤 Users

Users are one of the most common and important object types in Active Directory.

    They are known as security principals, meaning:

        They can be authenticated by the domain.

        They can be assigned permissions over resources (files, printers, etc.).

🧍‍♂️ Types of User Objects

    People
    Typically represent employees or individuals in the organization who need to access network resources.

    Services
    Represent services such as IIS or MSSQL.
    These users have only the permissions required to run their respective services.

💻 Machines

Each computer that joins the domain becomes a machine object in Active Directory.

    Machines are security principals too.

    They are assigned accounts similar to user accounts, but with limited domain rights.

    🛡️ Machine accounts are local administrators on their own systems but not intended for interactive use.

🔐 Machine Account Details

    Passwords are automatically rotated.

    Typically consist of 120 random characters.

    Named using the format:
    COMPUTERNAME$
    (e.g., DC01$ for a machine named DC01)

👥 Security Groups

Security groups allow administrators to manage permissions more efficiently:

    Permissions can be assigned to groups instead of individual users.

    Users and machines can be members of groups.

    Groups can even contain other groups (nested groups).

    Groups are also security principals.

🔒 Default Domain Security Groups
Security Group	Description
Domain Admins	Full administrative rights across the entire domain.
Server Operators	Can manage Domain Controllers, but not modify admin group memberships.
Backup Operators	Can access any file for backup, ignoring permissions.
Account Operators	Can create or modify user accounts in the domain.
Domain Users	Includes all user accounts in the domain.
Domain Computers	Includes all computer accounts in the domain.
Domain Controllers	Includes all Domain Controller machines.