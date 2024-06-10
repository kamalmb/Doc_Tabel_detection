import requests
import cv2
import random
import matplotlib.pyplot as plt
import os

class TableDetector:   
    def __init__(self,file_name):
        
        """ TableDetetctor constructor """

        self.API_URL = "https://api-inference.huggingface.co/models/TahaDouaji/detr-doc-table-detection"
        self.headers = {"Authorization": "Bearer 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"}
        self.file_name=file_name
        if not self.image_exists():
            raise FileNotFoundError(f"image {self.file_name} don't exist")
        self.response=None
        self.image=cv2.imread(file_name)
        

    def image_exists(self):
        """ function for image file verification  """
        return os.path.isfile(self.file_name)

    def post_data(self):
        """ Sends the content of a image to an API via a POST request and handles the response """
        with open(self.file_name, "rb") as f:
            data = f.read()
        try:
            self.response = requests.post(self.API_URL, headers=self.headers, data=data)
            self.Json_response=self.response.json()
            self.response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            # handel HTTP error
            if self.response.status_code == 503:
                # Handle HTTP error 503 and stop execution
                raise SystemExit(f"HTTP error 503: Service Unavailable - {err}")
            else:
                print(f"HTTP error: {err} with status code {self.response.status_code}")
                raise SystemExit(f"HTTP error : Service Unavailable - {err}")
        except requests.exceptions.RequestException as err:
            # handel an others possible http errors
            print(f"Request error: {err} with status code {self.response.status_code}")
    
    
    def get_file_name(self):
        """  get the image file name"""
        return self.file_name
    
    def get_image(self):
        """ get the image """
        return self.image
    
    def get_reponse(self):
        """ get the HTTP response """
        return self.response

    def Display_result(self):

        """ Displays the results of the detected objects from the API response in the terminal"""
        ### checks if the JSON response from the API contains any detected objects 
        if  not self.response.json():
            print("No Object Detected")
        for item in  self.response.json():
            # informations of each detected object
            score = item.get('score')
            label = item.get('label')
            box = item.get('box')

            if isinstance(box, dict):
                xmin = box.get('xmin')
                ymin = box.get('ymin')
                xmax = box.get('xmax')
                ymax = box.get('ymax')
                
                print(f"Label: {label}")
                print(f"Score: {score}")
                print(f"Box: (xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax})")

    
    def Display_on_image(self):

        """ Displays the results of the detected objects from the API response on the image """
        ### checks if the JSON response from the API contains any detected objects 
        if  not self.response.json():
            print("No Object Detected")
        for item in  self.response.json():
            # informations of each detected object
            score = item.get('score')
            label = item.get('label')
            box = item.get('box')

            ### generate diffrent colors for bounding boxs 
            color=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

            if isinstance(box, dict):
                xmin = box.get('xmin')
                ymin = box.get('ymin')
                xmax = box.get('xmax')
                ymax = box.get('ymax')

                # Draw the  bounding box
                cv2.rectangle(self.image, (xmin, ymin), (xmax, ymax), color, 2)
                
                # Display the label and the score
                text = f"{label}: {score:.2f}"
                cv2.putText(self.image, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
        # save the image 
        cv2.imwrite('Api_result.jpg',self.image)
        # Display the image with results
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

        
               