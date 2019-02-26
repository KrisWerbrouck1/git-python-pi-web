# PHPMyAdmin


## Installation

```
sudo apt install phpmyadmin -y
```

Setting a password for the root user

```
sudo mysql -u root
```

```
UPDATE mysql.user SET plugin = 'mysql_native_password', 
  Password = PASSWORD('NEWPASSWORD') WHERE User = 'root';
FLUSH PRIVILEGES;
```