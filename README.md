# barcode-scanner
A bunch of small solutions for qr codes and barcodes with python. Feel free to use and modify!

* [Reading the barcode/qrcode from a file](https://github.com/kor5n/barcode-project/edit/main/README.md#reading-the-barcodeqrcode-from-a-file-barcode2py)
* [Scanning the barcode iwth your computer camera](https://github.com/kor5n/barcode-project/edit/main/README.md#scanning-the-barcode-with-your-computer-camera-barcode_scannerpy)
* [Generating qrcode with graphical interface](https://github.com/kor5n/barcode-project/edit/main/README.md#scanning-the-barcode-with-your-computer-camera-barcode_scannerpy)

## Reading the barcode/qrcode from a file (barcode2.py)
To run the script type:
```
python3 barcode2.py -f <your file>
```
It will print the value of the code as well as showing how the program scanned the code for debugging and clarity.

## Scanning the barcode with your computer camera (barcode_scanner.py)
To run the script type:
```
python3 barcode_scanner.py
```
It will turn on your camera and open a window where the camera view is shown. When a barcode/qrcode is in the sight of your camera it will stop for a while and output the value of the code in the console.
> [!NOTE]
> If the code doesn't work then you should add permission to python or the console to use the computer camera.

## Generating qrcode with graphical interface (qr_code_generator.py)
To run the script type:
```
python3 qr_code_generator.py
```
It will open a window with the GUI. You can type som text into the input and then click the _"Create QR code"_ button which will genereate a qr code a the upper half of the window.
