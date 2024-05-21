import cv2
from pyzbar.pyzbar import decode
from argparse import ArgumentParser

def BarcodeReader(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Check if the image was successfully read
    if img is None:
        print("Error: Could not open or find the image.")
        return
    
    # Decode the barcode image
    detected_barcodes = decode(img)
    
    # If no barcode is detected, print the message
    if not detected_barcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detected_barcodes:
            # Locate the barcode position in the image
            (x, y, w, h) = barcode.rect
            
            # Put a rectangle around the barcode in the image
            cv2.rectangle(img, (x-10, y-10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
            
            # If barcode data is present, print it
            if barcode.data:
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type
                print(f"Data: {barcode_data}")
                print(f"Type: {barcode_type}")
    
    # Display the image with the detected barcodes
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parser to take the image file from the user
    parser = ArgumentParser(description='Process an image to detect barcodes.')
    parser.add_argument("-f", "--file", type=str, help="The barcode image to process", required=True)
    
    args = parser.parse_args()
    BarcodeReader(args.file)
