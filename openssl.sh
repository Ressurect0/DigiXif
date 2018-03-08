#! /bin/bash
rm image_dup.jpeg private.pem public.pem signature.bin signature_duplicate.bin
mv *.jp* image.jpeg
cp image.jpeg image_dup.jpeg
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
openssl dgst -sha256 -sign private.pem -out signature.bin image.jpeg
openssl dgst -sha256 -verify public.pem -signature signature.bin image.jpeg
exit