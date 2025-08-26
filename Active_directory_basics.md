# Windows Domain Core Concepts

The core of any Windows Domain is the **Active Directory Domain Services (AD DS)**. This service acts as a **catalogue** that holds the information of all the "objects" that exist on your network.

Among the many objects supported by AD DS, we have:

- Users
- Groups
- Machines
- Printers
- Shares
- And many more

Let's look at some of the key objects:

---

##  Users

Users are one of the most common object types in Active Directory. They are **security principals**, meaning they can be:

- Authenticated by the domain
- Assigned privileges over resources (e.g., files, printers)

### Types of Users:

1. **People**: Represent individuals (e.g., employees) who need access to the network.
2. **Services**: Represent services like IIS or MSSQL that require accounts to run.  
   > Service users typically have limited privileges tailored to their service.

---

##  Machines

Each computer that joins the domain becomes a **machine object** in AD.

- Machines are also **security principals** and have their own accounts.
- These accounts:
  - Are local administrators on their assigned computers
  - Are not meant for direct user access, but can be accessed if you have the password



### Naming Convention

- Machine accounts are named as:  
  **`<ComputerName>$`**
- Example: A machine named `DC01` will have an account: `DC01$`

---

##  Security Groups

Security groups help assign permissions to multiple users/machines at once.

- Easier management: Add users to a group to inherit its privileges
- Groups can:
  - Contain users, machines
  - Include other groups (nested)

### Default Domain Groups

| Security Group     | Description |
|--------------------|-------------|
| **Domain Admins**  | Full administrative control across the domain |
| **Server Operators** | Manage Domain Controllers but cannot change admin memberships |
| **Backup Operators** | Can access all files for backup, regardless of file permissions |
| **Account Operators** | Can create/modify user accounts in the domain |
| **Domain Users**   | Includes all user accounts in the domain |
| **Domain Computers** | Includes all computer objects in the domain |
| **Domain Controllers** | Includes all Domain Controllers in the domain |

---

