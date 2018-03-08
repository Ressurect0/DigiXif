import piexif, os, time

os.system("./openssl.sh")
time.sleep(3)
file = open("signature.bin","rb")
signature = file.read()
print "Signature: ",signature
print len(signature)
time.sleep(3)

# zeroth_ifd = {piexif.ImageIFD.Make: u"Canon",
#               piexif.ImageIFD.XResolution: (96, 1),
#               piexif.ImageIFD.YResolution: (96, 1),
#               piexif.ImageIFD.Software: u"piexif"
#               }
# gps_ifd = {piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
#            piexif.GPSIFD.GPSAltitudeRef: 1,
#            piexif.GPSIFD.GPSDateStamp: u"1999:99:99 99:99:99",
#            }
# first_ifd = {piexif.ImageIFD.Make: u"Canon",
#              piexif.ImageIFD.XResolution: (40, 1),
#              piexif.ImageIFD.YResolution: (40, 1),
#              piexif.ImageIFD.Software: u"piexif"
#              }
#
# exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
#             piexif.ExifIFD.LensMake: signature,
#             piexif.ExifIFD.Sharpness: 65535,
#             piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),
#             }
#
# exif_dict = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":gps_ifd, "1st":first_ifd, "thumbnail":thumbnail}
# exif_bytes = piexif.dump(exif_dict)
#
# print len(exif_bytes)
# piexif.insert(exif_bytes,"image.jpg")

exif_dict = piexif.load("image_dup.jpeg")
dict_value = piexif.ExifIFD.LensMake
exif_dict["Exif"] = {dict_value: signature}
# print exif_dict

exif_bytes = piexif.dump(exif_dict)
# print len(exif_bytes)

piexif.insert(exif_bytes,"image_dup.jpeg")

exif_dict = piexif.load("image_dup.jpeg")
signature_copy = exif_dict["Exif"][dict_value]
os.system("clear")
time.sleep(3)
print "Signature Copy Retreived..............."
time.sleep(3)
print signature_copy
time.sleep(3)

file = open("signature_duplicate.bin","wb")
file.write(signature_copy)

os.system("clear")
print "Run ./verify_ds.sh to verify the Retrieved Signature from the signed image."