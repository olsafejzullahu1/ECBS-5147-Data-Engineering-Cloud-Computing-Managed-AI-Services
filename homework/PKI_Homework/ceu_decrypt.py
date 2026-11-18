
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load CEU's private key
with open("ceu_key", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

# Read the encrypted message
with open("encrypted_message.bin", "rb") as file:
    encrypted_message = file.read()

# Decrypt the message
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print the original message
print("Decrypted message:")
print(decrypted_message.decode("utf-8"))