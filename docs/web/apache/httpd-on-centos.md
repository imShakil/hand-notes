Configure **firewalld** to Allow Apache Traffic

In a standard installation, CentOS 7 is set to prevent traffic to Apache.

Normal web traffic uses the http protocol on Port 80, while encrypted web traffic uses the https protocol, on Port 443.

1. To get the active zones of apache server

```
firewall-cmd --get-active-zones
```

1. Modify your firewall to allow connections on these ports using the following commands:
```text
sudo firewall-cmd ––permanent ––add-port=80/tcp
sudo firewall-cmd ––permanent ––add-port=443/tcp
```

2. Once these complete successfully, reload the firewall to apply the changes with the command:

```
sudo firewall-cmd ––reload
```



This is going to help if the port is closed due to some unnecessary issue.
