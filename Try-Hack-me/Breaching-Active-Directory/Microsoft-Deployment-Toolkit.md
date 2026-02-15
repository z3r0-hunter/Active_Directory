### What is Microsoft Deployment Toolkit (MDT)?

- MDT is a free tool from Microsoft used for automated deployment and installation of operating systems on a large number of devices within an organization, without direct manual intervention.

- Why is MDT used in large organizations?

  - In corporate environments with hundreds or thousands of devices:

     - Administrators cannot manually install the system (using DVD or USB) on each device.

         - Instead:

             - A custom Windows image is created, which includes:

             -  Required software (such as Office or antivirus)

             - System settings

             - User permissions

       - This image is then automatically sent to new devices over the network using PXE Boot.

### Difference between MDT and SCCM:
- Tool	Function
  MDT	Used for creating and deploying Windows images automatically (OS deployment).
 SCCM	Used for system management post-installation: updates, applications, patches (Patch Management).

   - SCCM is considered the "big brother" of MDT.

### What is PXE Boot?

- PXE = Preboot eXecution Environment

- PXE is a method that allows a computer without an operating system to boot over the network (Network Boot).

- How does PXE Boot work?

   - The device sends a request to the DHCP server.

   - DHCP responds with an IP address and the server address containing the PXE Boot image (MDT Server).

   - The device establishes a connection with TFTP to download the BCD file and installation files.

   - The system installation begins automatically using the pre-configured settings in MDT.

#### From a hacker or penetration tester's perspective:

- What can be exploited:

    - Exploiting PXE Boot to deploy an image with a backdoor:

    - Example: Adding a local admin user during the automated system installation.

    - Password Scraping:

      - Sometimes, during the automated installation:

      -  AD accounts for certain services are used.

     - These accounts might temporarily be stored in files like unattended.xml or other locations.

   - As an attacker, you can analyze PXE boot files and extract these accounts.

