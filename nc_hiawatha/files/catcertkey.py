#! /usr/bin/env python3

import hashlib
import logging
import sys
import pathlib

FULLCERT = "fullchain.pem"
PRIVKEY = "privkey.pem"
KEYCERT = "key_plus_cert.pem"

log = logging.getLogger(__name__)


def concat_key_cert(certdir):
    """
    Concatenates the files 'privkey.pem' and 'fullchain.pem' in the
    directory into a key_cert file, only if they are different from the
    current contents of the present contents of the key_cert file, or
    if key_cert does not exist
    """
    cert = certdir / FULLCERT
    key  = certdir / PRIVKEY
    keycert = certdir / KEYCERT

    with key.open("rb") as kfd:
        content  = kfd.read()
    with cert.open("rb") as cfd:
        content += cfd.read()

    checksum = hashlib.sha256(content).digest()

    if keycert.is_file():
        with keycert.open("rb") as kcfd:
            checksum_current = hashlib.sha256(kcfd.read()).digest()
    else:
        checksum_current = b""

    if checksum != checksum_current:
        log.info("Writing new file '{}'".format(str(keycert)))
        with keycert.open("wb") as kcfd:
            kcfd.write(content)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 0:
        log.error("certdir not specified on command line. Exiting.")
        return 1

    maindir = pathlib.Path(argv[0])
    if not maindir.is_dir():
        log.error("Path '{}' is not a directory.".format(maindir))
        return 2

    for cd in maindir.iterdir():
        if cd.is_dir():   # a dir holding certificates
            concat_key_cert(cd)

    return 0


if __name__ == "__main__":
    try:
        rc = main(sys.argv[1:])
    except:
        log.error("Exception.", exc_info=True)
        rc = 127
    sys.exit(rc)
