
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load CEU's public key
with open("ceu_key.pub", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

# Create a message
message = b"Hello CEU! This is my encrypted message."

# Encrypt the message using CEU's public key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the encrypted message to a file
with open("encrypted_message.bin", "wb") as file:
    file.write(encrypted_message)

print("Message encrypted and saved successfully!")
