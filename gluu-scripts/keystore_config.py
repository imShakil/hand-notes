#!/usr/bin/python3

import os
import subprocess

keytool = "/opt/amazon-corretto-11.0.14.10.1-linux-x64/bin/keytool"
defaultTrustStoreFN = "/opt/amazon-corretto-11.0.14.10.1-linux-x64/jre/lib/security/cacerts"
defaultTrustStorePW = "changeit"
host = "test.gluu.org"
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
        subprocess.call([keytool, "-importcert", "-file", (cert_folder+"{}.crt").format(crt_name), "-keystore", defaultTrustStoreFN, "-alias", (host+"_{}").format(crt_name), "-storepass", defaultTrustStorePW])
    except Exception as e:
        print(e, " for ", crt_name)


def config_keystore():
    delete_keys = ["idp-signing", "idp-encryption"]
    import_keys = ["idp-signing", "idp-encryption"]

    for item in delete_keys:
        delete_key(item)
    
    for item in import_keys:
        import_key(item)

config_keystore()
