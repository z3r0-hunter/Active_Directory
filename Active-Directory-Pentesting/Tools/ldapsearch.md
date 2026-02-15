# What is ldapsearch
  - commond line untilies used to perform LDAP searchs
  - part of the OpenLDAP or LDAP utitlies package
  -  used to search and retrieve data from LDAP directory server , such as Active directory , OpenLDAP

# Command 
  - display all users and groups and computers
    - Example
    ```
    ldapsearch -x -H ldap://domain_controller_ip -D "standard_user_to_enum" -w "password" -b "DC=example,DC=com" "objectclass=" 
    ```
    - at objectclass can write **user** or **groups** or **computers**
    - -H : The URL of the ldap  server
    - -b : the base DN
    - -D : The distinguished name 
    - -w : the password for authentication
    
