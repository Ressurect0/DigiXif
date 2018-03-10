<img src="https://github.com/SanjeetSR/DigiXif/blob/master/images/text4033.png" margin="0px" height="36px" width="110px"/>Digitally Signing Images using RSA 2048 and Embedding Signatures within the Exif Metadata of the Image.

Pre-requisites
--------------
sudo apt-get install python  
sudo apt-get install python-setuptools python-dev build-essential  
sudo apt-get install python-pip  
pip install piexif  
chmod 777 openssl.sh  
chmod 777 verify_ds.sh  

Running
-------
python digital_signed_image.py  

![alt text](https://github.com/SanjeetSR/DigiXif/blob/master/images/screen_1.png) 

Verifying Signatures 
--------------------
openssl dgst -sha256 -verify public.pem -signature signature_duplicate.bin image.jpeg  
or   
./verify_ds.sh

![alt text](https://github.com/SanjeetSR/DigiXif/blob/master/images/screen_2.png)  

Pending Modifications
---------------------
* Adding Public certificate in another Exif Metadata Tag.  
 


