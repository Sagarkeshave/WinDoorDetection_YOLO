

from gradio_client import Client, handle_file
import os 

client = Client("SagarKeshave/WinDoorDetection_YOLO")
result = client.predict(
		image=handle_file(r'test_image/22.png'),
		api_name="/predict"
)
print(f"result: \n{result}")