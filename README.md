![Banner](banner.png)

## Crypto-Cipher

Crypto-Cipher encrypts and decrypts short text strings with Fernet
symmetric encryption, and generates Fernet keys. It works on text given
on the command line only; there is no file input or output mode.

### Installation

```
pip install -r requirements.txt
```

### Usage

```
python main.py generate-key
python main.py encrypt --key <fernet-key> --text "Hello, world!"
python main.py decrypt --key <fernet-key> --text <token-from-encrypt>
```

The key must be a real Fernet key, as produced by `generate-key`; an
arbitrary password string is not accepted. A failed run (bad key, bad
token, or a missing `--key` or `--text`) prints an error and exits 1.

### Security Warnings

* Keep your encryption keys confidential.
* Ensure the security of the communication channel while exchanging keys.

### License

Copyright (c) CY83R-3X71NC710N

Crypto-Cipher is licensed under the GNU General Public License v3.0.
