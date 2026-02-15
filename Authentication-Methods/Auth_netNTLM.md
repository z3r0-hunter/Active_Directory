# 🔓 NetNTLM Authentication – Legacy Protocol

## 📌 What is NetNTLM?

NetNTLM is a legacy **challenge-response** authentication protocol used in Windows environments when Kerberos is not available. It allows users to authenticate **without sending their password or hash** directly over the network.

It is often used in:
- SMB (file shares)
- HTTP (IIS, intranet portals)
- Legacy systems & third-party apps

---

## 🔐 How NetNTLM Works – Step-by-Step

1. **Client → Server**:  
   The user initiates a connection and requests to authenticate.

2. **Server → Client**:  
   The server responds with a random **challenge** (nonce).

3. **Client**:  
   The client generates a **response hash** using:
   - The challenge
   - The user's **NTLM password hash**
   - Known metadata (username, domain)

4. **Client → Server**:  
   The response is sent back to the server.

5. **Server → Domain Controller**:  
   The server forwards the username, challenge, and response to the **DC**.

6. **Domain Controller**:  
   Recomputes the expected response using the stored NT hash.
   - ✅ If it matches: authentication is successful.
   - ❌ If not: access is denied.

---

## 🧪 Real-World Attacks Against NetNTLM

### 🚨 1. **NTLM Relay Attacks**
- Attacker tricks the user into authenticating to a **malicious server**.
- The attacker forwards the NTLM response to a **real server** and gains access.

**Tools**:  
- `ntlmrelayx.py` (Impacket)  
- `PetitPotam` + `NTLM relay`

---

### 🚨 2. **Credential Harvesting**
- Tools like **Responder** or **Inveigh** act as fake SMB/HTTP servers.
- They capture **NetNTLMv1/v2 hashes** from clients automatically.
- These hashes can then be cracked offline.

---

### 🚨 3. **Pass-the-Hash (PtH)**
- If attacker gets the NTLM hash of a user, they can authenticate directly **without password**.

---

## 🛡️ How to Defend Against NetNTLM Attacks

✅ **Best Practices for Hardening**:

- 🚫 **Disable NTLM** authentication when possible via Group Policy:
