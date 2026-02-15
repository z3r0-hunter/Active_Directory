# 🔐 AD Authentication Methods

## 📌 Overview

In Windows domain environments, authentication is a critical function. All credentials are stored within **Domain Controllers (DCs)**, and any time a user tries to access a domain-based resource, the **DC** is contacted to validate the credentials.

Windows supports two main authentication protocols:

- **Kerberos** (Default, modern)
- **NetNTLM** (Legacy, but often still enabled)

---

## 🦾 Kerberos Authentication – Modern, Ticket-Based System

### 🔁 General Idea

Kerberos works by issuing **tickets** that prove a user has already been authenticated. Once a user obtains a **TGT (Ticket Granting Ticket)**, they can request **TGS (Ticket Granting Service)** tickets to access specific services **without resending their password**.

---

### 🔐 Step-by-Step Flow

#### 🧩 Step 1: User Authentication to the KDC

- The user sends: `username + timestamp`, encrypted with a key derived from their password.
- Sent to the **KDC (Key Distribution Center)** – usually the Domain Controller.

➡️ **KDC responds with:**

- **TGT**: Encrypted with the `krbtgt` account's password hash.
- **Session Key**: Used for further secure communication.

📌 *The user cannot read the contents of the TGT — it is encrypted. However, it contains a copy of the Session Key.*

---

#### 🧩 Step 2: Requesting a Service Ticket (TGS)

When the user wants to access `\\fileserver\share`, they send:

- Their **TGT**
- A request with `username + timestamp` encrypted with the Session Key
- The **SPN (Service Principal Name)** of the target service

➡️ **KDC responds with:**

- **TGS**: A ticket for the specific service (e.g., File Server), encrypted using the service account’s password hash
- **Service Session Key**

📌 *Only the target service can decrypt this ticket and retrieve the session key.*

---

#### 🧩 Step 3: Accessing the Service

- The user sends the **TGS** to the service (e.g., File Server).
- The service uses its own credentials to decrypt the TGS, verify the Session Key, and grant access.

---

## 🧪 Real-World Attacks During This Phase

### 🚨 Attacks that can happen here:

- **Golden Ticket Attack**: Forging a TGT using the `krbtgt` hash to impersonate any user, including Domain Admins.
- **Pass-the-Ticket**: Reusing a stolen valid ticket (TGT or TGS) to access services without knowing the password.
- **Pass-the-Hash**: Using NTLM hashes directly to authenticate without needing the actual password.

---

## 🛡️ How Can Prevent These Attacks

- 🔄 Regularly rotate the **krbtgt** account password (twice in succession).
- 🔐 Enable **Account Lockout Policies** to detect brute-force attempts.
- 🧱 Use **LSA Protection** and restrict access to **LSASS memory** (prevent ticket dumping).
- 📏 Enforce **Strong Password Policies** on all service accounts.
- 🛡️ Implement **Kerberos Armoring (FAST)** to protect Kerberos traffic.
- 🧑‍💼 Use **tiered administration**: avoid logging into lower-trust systems with privileged accounts.

---

### Note
- Kerberos run im port `88 ` and protocol `TCP/UDP` 
