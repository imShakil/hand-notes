#!/usr/bin/python3

import os
import subprocess

keytool = "/opt/jre/bin/keytool" # change this according to version
defaultTrustStoreFN = "/opt/jre/jre/lib/security/cacerts"
defaultTrustStorePW = "changeit"
host = "test.gluu.org" # replace with accurate host name
cert_folder = "/etc/certs/"

def delete_key(crt_name):
    if os.path.isfile((cert_folder+"{}.crt").format(crt_name)):
        try:
            subprocess.call([keytool, "-delete", "-alias", (host+"_{}").format(crt_name), "-keystore", defaultTrustStoreFN, "-storepass", defaultTrustStorePW])
        except Exception as e:
            print(e, " for ", crt_name)


def import_key(crt_name):
    #print((cert_folder+"{}.crt").format(crt_name))
    try:
        subprocess.call([keytool, "-importcert", "-file", (cert_folder+"{}.crt").format(crt_name), "-keystore", defaultTrustStoreFN, "-alias", (host+"_{}").format(crt_name), "-storepass", defaultTrustStorePW, "-noprompt"])
    except Exception as e:
        print(e, " for ", crt_name)


def config_keystore():
    # add list here to delete / import keys from
    delete_keys = ["httpd", "idp-signing", "idp-encryption"]
    import_keys = ["httpd", "idp-signing", "idp-encryption"]

    for item in delete_keys:
        delete_key(item)
    
    for item in import_keys:
        import_key(item)

config_keystore()
