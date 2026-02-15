# Managing Computers in Active Directory

## 📝 Notes

- By default, all machines that join a domain are placed in the built-in container called `Computers`.

- Keeping all devices in this default container is **not ideal**, as it's likely you will want to apply different policies for different types of machines (e.g., servers vs. workstations).

- It's a good practice to **categorize** your devices into at least the following three groups:

---

### 🖥️ Workstations

- Used for day-to-day work and general browsing activities.
- Typically assigned to end users.
- May have limited privileges based on organizational policies.

---

### 🖧 Servers

- Provide services to users or other systems (e.g., file servers, application servers).
- Require more security and management policies compared to workstations.

---

### 🛡️ Domain Controllers

- Responsible for managing **Active Directory**.
- Store all user accounts and **hashed passwords**.
- Central to the security and identity infrastructure of the domain.
