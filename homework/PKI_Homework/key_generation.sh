
#!/bin/bash

# Generate CEU's private key
openssl genpkey -algorithm RSA -out ceu_key -pkeyopt rsa_keygen_bits:2048

# Generate CEU's public key
openssl pkey -in ceu_key -pubout -out ceu_key.pub

# Restrict access to the private key
chmod 600 ceu_key

echo "CEU keys generated successfully!"
