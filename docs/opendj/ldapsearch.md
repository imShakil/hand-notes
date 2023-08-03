
# To count total users in opendj backends:

```text
/opt/opendj/bin/ldapsearch -h localhost -p 1636 -Z -X -D "cn=directory manager" -w <password> -b 'o=gluu' 'oxAuthGrantId=*' dn | grep 'dn:' | wc -l
``` 

# To Find a specific user using its `uid`:

```
/opt/opendj/bin/ldapsearch -h localhost -p 1636 -Z -X -D "cn=directory manager" -w "password" -b 'o=gluu' "(uid=admin)"
```
