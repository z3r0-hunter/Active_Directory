#  What is `rpcclient`

##  What is RPC?
- **RPC (Remote Procedure Call)** is a communication protocol that allows a program to execute code (procedures) on another computer in the network.
- Commonly used in **Windows environments** for interaction between services and applications.
- Built on **Microsoft COM and DCOM technologies**.
- Communicates over **SMB protocol** (usually port 445).
- Extensively used in Active Directory for communication with Domain Controllers.

---

##  What is `rpcclient`?
- `rpcclient` is a command-line tool included with the **Samba suite** (commonly used on Linux/Kali).
- It is designed for:
  - **Debugging**
  - **Testing**
  - **Enumerating** remote Windows services via RPC.
- Enables interaction with Windows systems (especially **Active Directory**) without a GUI.

---

##  How to Use `rpcclient` in Active Directory Enumeration

Once you have **valid credentials or null session access**, run:

```bash
rpcclient -U "%" <target_ip>
```

Or with credentials:

```bash
rpcclient -U 'username%password' <target_ip>
```

---

##   Commands in AD Enumeration

| Command | Description |
|---------|-------------|
| `srvinfo` | Return server information |
| `querydominfo` | Return domain information |
| `enumdomusers` | Enumerate domain users |
| `enumdomgroups` | Enumerate domain groups |
| `querygroup <RID>` | Get group details |
| `queryuser <RID>` | Get user details |
| `enumprivs` | Enumerate privileges |
| `getdompwinfo` | Get domain password info |
| `getusrdompwinfo <RID>` | Get user-specific password info |
| `lsaenumsid` | Enumerate SIDs from LSA |
| `createdomuser <username>` | Create a domain user |
| `setuserinfo2 <username> 24 <password>` | Set password for user |
| `lookupnames <username>` | Check if user has a SID assigned |
| `enumalsgroups builtin` | Enumerate alias groups |
| `deletedomuser <username>` | Delete domain user |
| `netshareenum` | Enumerate network shares |
| `netsharegetinfo <sharename>` | Get info of network share |
| `enumdomains` | Enumerate multiple domains |
| `chgpasswd <user> <old_pass> <new_pass>` | Change password of a user |
| `samlookupnames domain <username>` | Extract RID of a specific user |

---

> These commands are extremely useful for internal enumeration during an Active Directory penetration test.