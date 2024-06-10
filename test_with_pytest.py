import pytest
from Tabledetector import TableDetector
import os

filename ="Bank-doc.jpg"
# Create an instance of TableDetector with a specified filename
tabledetector=TableDetector(filename)

def test_get_data():
    """ Test that the POST request returns a successful response and non-null JSON data   """
    #we assume that the service is available  
    _=tabledetector.post_data()
    assert tabledetector.get_reponse().status_code==200
    assert tabledetector.get_reponse().json() is not None


def test_image_exist():
    """ Test that the image file exists  """
    image=tabledetector.get_file_name()
    assert os.path.isfile(image)

def test_image_not_exist():
    """ Test that the image file exists  """
    filename ="image_not_exist.jpg"
    # Create an instance of TableDetector with a specified filename
    with pytest.raises(FileNotFoundError) as excinfo:
        TableDetector(filename)
    assert str(excinfo.value) == f"image {filename} don't exist"
    
def test_image_not_null():
    """ Test that the image file  don't exists or we can't read the image """
    assert tabledetector.get_image() is not None


if __name__ == "__main__":
    # run tests with pytest
    pytest.main(["-v"])