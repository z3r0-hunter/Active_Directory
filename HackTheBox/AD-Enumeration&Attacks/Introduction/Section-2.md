# Active Directory Reconnaissance & Enumeration Tools (Summary)

##  PowerShell & .NET Tools
- **PowerView / SharpView**  
  AD situational awareness (users, groups, computers, attack paths like Kerberoasting/ASREPRoasting).

- **SharpHound**  
  Collects AD data (users, groups, sessions, ACLs, GPOs) → outputs JSON for BloodHound.

- **Inveigh.ps1**  
  Network spoofing/poisoning (LLMNR, NBT-NS, MDNS) to capture credentials.

- **C# Inveigh (InveighZero)**  
  C# version with interactive console for captured hashes/credentials.

- **DomainPasswordSpray.ps1**  
  Password spraying against AD users.

- **LAPSToolkit**  
  Auditing and attacking environments using Microsoft LAPS.

- **setspn.exe**  
  Manage and enumerate Service Principal Names (SPNs).

---

##  Python-Based Tools (Impacket)
- **BloodHound.py**  
  AD data ingestor for BloodHound (works without domain join).

- **GetUserSPNs.py**  
  SPN enumeration for Kerberoasting.

- **GetNPUsers.py**  
  ASREPRoasting (extract AS-REP hashes).

- **secretsdump.py**  
  Dump SAM/LSA secrets remotely.

- **psexec.py**  
  Remote shell execution (PsExec-like).

- **wmiexec.py**  
  Command execution via WMI.

- **mssqlclient.py**  
  MSSQL database interaction.

- **ntlmrelayx.py**  
  SMB relay attack framework.

- **rpcdump.py**  
  RPC service enumeration.

- **ticketer.py**  
  Kerberos ticket manipulation (Golden Ticket, etc.).

- **raiseChild.py**  
  Child-to-parent domain privilege escalation.

- **gettgtpkinit.py**  
  Kerberos certificate/TGT manipulation.

- **getnthash.py**  
  Extract NT hashes via Kerberos.

- **lookupsid.py**  
  SID brute-forcing tool.

---

##  Data Visualization & Analysis
- **BloodHound**  
  Graph-based AD relationship mapping (Neo4j + GUI).

- **Active Directory Explorer**  
  View/edit AD database, compare snapshots.

- **ADRecon**  
  AD data extraction → Excel reports with security analysis.

---

##  Credential & Hash Tools
- **Mimikatz**  
  Password extraction, pass-the-hash, Kerberos ticket dumping.

- **Hashcat**  
  Password/hash cracking tool.

- **gpp-decrypt**  
  Extract credentials from Group Policy Preferences.

---

##  Network & Protocol Tools
- **Responder**  
  LLMNR/NBT-NS poisoning for credential capture.

- **ldapsearch**  
  LDAP directory queries.

- **windapsearch**  
  Automated LDAP enumeration (users, groups, computers).

- **rpcinfo**  
  RPC service enumeration.

- **rpcclient**  
  Samba-based AD enumeration via RPC.

- **adidnsdump**  
  DNS zone/record enumeration from AD.

---

##  Exploitation & Post-Exploitation
- **CrackMapExec (CME)**  
  Multi-protocol AD attack & enumeration framework (SMB, WinRM, WMI, MSSQL).

- **Kerbrute**  
  Kerberos-based enumeration, brute force, password spraying.

- **Rubeus**  
  Kerberos abuse toolkit.

- **evil-winrm**  
  Remote interactive shell over WinRM.

- **noPac.py**  
  Exploits CVE-2021-42278 & CVE-2021-42287 for DA escalation.

- **CVE-2021-1675.py (PrintNightmare)**  
  Privilege escalation PoC.

- **PetitPotam.py**  
  MS-EFSRPC coercion attack.

---

##  File & Share Enumeration
- **smbmap**  
  SMB share enumeration.

- **Snaffler**  
  Finds sensitive files/credentials on shares.

- **smbserver.py**  
  Lightweight SMB server for file transfer.

- **enum4linux / enum4linux-ng**  
  SMB/Samba enumeration tools.

---

##  Auditing & Security Assessment
- **PingCastle**  
  AD security risk scoring and maturity assessment.

- **Group3r**  
  GPO security misconfiguration auditing tool.