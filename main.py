import argparse
import logging
import sys
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Setup command line argument parsing.
    """
    parser = argparse.ArgumentParser(
        description="Text encryption and decryption tool using Fernet symmetric encryption."
    )
    parser.add_argument(
        "operation", choices=["encrypt", "decrypt", "generate-key"],
        help="Operation to perform: encrypt, decrypt, or generate-key."
    )
    parser.add_argument(
        "--key", help="Encryption/Decryption key (required for encrypt/decrypt)."
    )
    parser.add_argument(
        "--text", help="Text to encrypt or decrypt (required for encrypt/decrypt)."
    )
    return parser

def main():
    """
    Main function to handle encryption, decryption, and key generation.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    try:
        # This branch runs before any key or text check, so passing
        # --key or --text with generate-key is silently ignored
        # rather than treated as a mistake.
        if args.operation == "generate-key":
            # Generate a new key
            # I print the key and log it at info level as well. Anyone who
            # keeps this program's logs has a copy of the key, which is
            # worth knowing before this is run anywhere shared.
            key = Fernet.generate_key()
            logging.info("Generated encryption key: %s", key.decode())
            print(key.decode())

        elif args.operation == "encrypt":
            if not args.key or not args.text:
                raise ValueError("Both --key and --text are required for encryption.")
            # I take the text only from the command line. There is no file
            # or standard input path, so long text and text with shell
            # special characters have to survive the caller's quoting.
            fernet = Fernet(args.key.encode())
            encrypted_text = fernet.encrypt(args.text.encode()).decode()
            logging.info("Encryption successful.")
            print(encrypted_text)

        elif args.operation == "decrypt":
            if not args.key or not args.text:
                raise ValueError("Both --key and --text are required for decryption.")
            fernet = Fernet(args.key.encode())
            decrypted_text = fernet.decrypt(args.text.encode()).decode()
            logging.info("Decryption successful.")
            print(decrypted_text)

        else:
            logging.error("Invalid operation. Use encrypt, decrypt, or generate-key.")
            parser.print_help()

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print(f"Error: {str(e)}")
        # Every failure used to fall through to exit 0, so a script could
        # not tell a failed decryption from a good one without reading the
        # output text. Fernet also raises with an empty message for a bad
        # token, which is why the printed error above can look blank.
        sys.exit(1)

if __name__ == "__main__":
    main()