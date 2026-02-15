
#  NTLM Authentication in Active Directory – Simplified Explanation with Practical Examples

##  What is NTLM?
NTLM (NT LAN Manager) is a **challenge-response authentication protocol** used in Windows environments before Kerberos became the default. It is still used in legacy systems and sometimes falls back when Kerberos fails.

---

##  Types of Hashes and Protocols
| Name     | Type        | Uses Crypto | Mutual Auth | Relies on DC | Secure? |
|----------|-------------|-------------|-------------|--------------|---------|
| LM       | Hash        | DES         | ❌           | ❌            |  Very weak |
| NTLM     | Hash        | MD4         | ❌           | ✅            |  Weak |
| NTLMv1   | Protocol    | MD4         | ❌           | ✅            |  Weak |
| NTLMv2   | Protocol    | HMAC-MD5    | ❌           | ✅            | ✅ Better |
| Kerberos | Protocol    | DES/MD5/PK  | ✅           | ✅            | ✅ Stronger |

---

##  LM Hash – (VERY WEAK!)
- Max 14-character passwords (not case-sensitive).
- Converts to UPPERCASE and splits into 7-char chunks.
- Uses DES encryption on "KGS!@#$%".
- Very fast to crack (using Hashcat or similar).
- **Avoid using LM hashes** – disable them via Group Policy.

 Example: `299bd128c1101fd6`

---

##  NT Hash (NTLM)
- Uses MD4 on the UTF-16LE password.
- Stored in **SAM** (local) or **NTDS.DIT** (Domain Controller).
- Used in NTLMv1/v2 authentication.

 Example: `b4b9b02e6f09a9bd760f388b67351e2b`

---

##  How NTLM Works (Challenge-Response)

1. Client → Server: NEGOTIATE message
2. Server → Client: CHALLENGE message (random number)
3. Client → Server: AUTHENTICATE message (response = NT hash + challenge)

 Server → Domain Controller: verifies hash response (via SAMR/Netlogon)

---

##  Attacks on NTLM
- **Pass-the-Hash**: Use NTLM hash to authenticate without knowing password.
- **Relay Attack**: Relay captured NTLM auth to other service.
- **Offline Cracking**: Brute-force hash using tools like Hashcat.

---

##  NTLMv1 – NetNTLMv1 (Weak)

- Uses LM or NT hash to produce a **24-byte response**.
- Not pass-the-hash compatible.
- Easy to crack after capture.

**Capture via Responder or NTLM Relay**

---

##  NTLMv2 – NetNTLMv2 (Improved)

- Default on modern Windows.
- Uses HMAC-MD5 with challenge + user info + time.
- More complex and secure than NTLMv1.

**Still crackable with dictionary + rules + GPU**

---

##  Domain Cached Credentials (DCC/MSCache2)
- Stored locally for offline logins (when DC is unreachable).
- Format: `$DCC2$10240#bjones#e4e938d12fe5974dc42a90120bd9c90f`
- Slow to crack, can’t be used for pass-the-hash.
- by default Hosts save the last **ten** hashes for any domain users that successfully log into the machine in the HKEY_LOCAL_MACHINE\SECURITY\Cache registry key

**Requires local admin access to extract.**

---
- As a pentester, learn to:
   - Detect hash types
   - Crack when feasible
   - Use replay where allowed
   - Spot weaknesses in authentication fallbacks