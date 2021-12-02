# install the module
# pip install myqr

from MyQR import myqr

## to generate normal qr code
myqr.run('http://bit.ly/hackersrealm', save_name='qrchannel.png')

## to generate customized qr code
myqr.run(words='http://bit.ly/hackersrealm', picture='test-image.jpg',
         colorized=True, save_name='qrchannelcustomized.png')
