from Tabledetector import TableDetector
import time

if __name__ == "__main__":
    # the image name to be processed
    image_name = "Bank-doc.jpg"
    # Create an instance of TableDetector 
    my_table_detector = TableDetector(image_name)

    start_time = time.time()
    # Send the POST request to the API
    my_table_detector.post_data()
    end_time = time.time()
    
    # Calculate the response time
    response_time = end_time - start_time
    print(f"API response time: {response_time} seconds")
    
    # Display the results of the detected objects from the API response
    my_table_detector.Display_result()
    
    # Display the detected objects on the image
    my_table_detector.Display_on_image()
