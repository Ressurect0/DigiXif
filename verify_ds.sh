#! /bin/bash
openssl dgst -sha256 -verify public.pem -signature signature_duplicate.bin image.jpeg
exit