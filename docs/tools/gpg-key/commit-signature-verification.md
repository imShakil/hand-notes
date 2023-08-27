# To install gnupg 
```text
sudo apt-get install gnupg
```

# To Generate gpg key with details
```text
gpg --full-generate-key
```

# TO display text format public key
```text
gpg --armor --export [email-id/key] > gpg.key

cat gpg.key
```
# Add this key into github

To know the process about "how to add GPG key in github?" please follow this link: https://medium.com/big0one/how-to-create-a-verified-commit-in-github-using-gpg-key-signature-16acee004e0f

# Add this key into local git client

```
$ git config --global user.signingkey [secret-key]
$ git config --global commit.gpgsign true
$ git config --global gpg.program $(which gpg)
```
# To find secret key

```
$ gpg --list-secret-keys --keyid-format=long
```

After then choose the secret key formatted as rsa.../secret key

# Commit Signature Verification

```text
git commit -S -m "msg"
```
