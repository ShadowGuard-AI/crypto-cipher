![A single long leg crossing the porch boards in the foreground with its joint high, the harvestman beyond it in its corner with its remaining legs around it, and further along the porch a chair leg, a broom, a shut screen door, and a whole moth resting on the door frame, with no text, no letters, no wordmark, and no logo](intro-banner.png)

# crypto-cipher

Title block: a field guide entry, common name first and no Latin invented for a programme. The name above is set in Big Shoulders Stencil Display in rust on river white, ruled beneath, with a small harvestman beside this first heading only. The remaining headings keep the entry form without the creature.

![One harvestman at rest in a porch corner: a single small unsegmented oval body, eight long legs in two groups of four, each bent once high with rust at the joints, kingfisher teal boards behind and reed skirting at the floor line, with the name in field guide lettering below](logo.png)

![Late light along a porch stopping in one corner: boards running toward a shut screen door, a chair leg and a broom in the middle distance, the harvestman high on its legs in the angle with its shadow thrown long, and a small painted name board beside the door carrying the name, the only lettering in the scene](banner.png)

![The porch in three bands: the far screen door where the light fades slowly and the door never opens, the corner in the middle band where the harvestman lifts one leg at long intervals and sets it down a board further on, and the near board edge across which one whole beetle crosses once and is gone](scene.svg)

![Major separator](sep-heavy.svg)

## Crypto-Cipher

> Painted board nailed beside the chapter: this tool has no file mode. It reads no files, writes no files, and takes no standard input path; it works only on text handed to it on the command line.

![Minor separator](sep-light.svg)

Crypto-Cipher encrypts and decrypts short text strings with Fernet

symmetric encryption, and generates Fernet keys. It works on text given

on the command line only; there is no file input or output mode.

### Installation

> Painted board nailed beside the chapter: a generated key also enters the log. Key generation prints the new key on its own line and also writes that same key into the programme log at information level, so anyone who keeps the log of a generation run keeps a copy of what was generated.

![Minor separator](sep-light.svg)

```

pip install -r requirements.txt

```

### Usage

> Painted board nailed beside the chapter: extra arguments beside generation are quietly ignored rather than treated as an error, because the code takes the generation branch before it checks anything else.

![Minor separator](sep-light.svg)

```

python3 main.py generate-key

python3 main.py encrypt --key <fernet-key> --text "Hello, world!"

python3 main.py decrypt --key <fernet-key> --text <token-from-encrypt>

```

The key must be a real Fernet key, as produced by `generate-key`; an

arbitrary password string is not accepted. A failed run (bad key, bad

token, or a missing `--key` or `--text`) prints an error and exits 1.

### Verified run note

> Painted board nailed beside the chapter: a bad token can produce an error line whose message is empty, because the underlying library raises it that way. A blank looking error is still a failure and still exits 1.

![Minor separator](sep-light.svg)

The commands above are taken from the argument parser in `main.py`. A live run in this environment is blocked because the `cryptography` package is not installed here, so even `--help` stops at that import; no run result is claimed for this tool.

### Security Warnings

* Keep your encryption keys confidential.

* Ensure the security of the communication channel while exchanging keys.

### License

Crypto-Cipher is licensed under the GNU General Public License v3.0. See LICENSE.

![Major separator](sep-heavy.svg)

## Facts from the code, stated in the prose

This record names: Fernet, generate-key, encrypt, decrypt, --key, --text, positional, exits 0, exits 1, information level, cryptography, 41.0.0, GNU General Public License v3.0, python3 main.py.
