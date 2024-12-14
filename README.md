To run the file:
Downlod the zip file, Extract the python file within,
Change the connection string and adjust the Light_Timeout parameter accordingly,
Download and install the Azure IOT cli,
Run command az login, This will lead to an OAuth page to log you in your Azure account,
After a successfull login, Run command "az iot hub monitor-events --hub-name <YourIoTHubName> --device-id <YourDeviceId>"
Make sure the YourIoTHubName and YourDeviceId are changed to your parameters.
Run the python file in your computer,
This will start a log report on the cli giving you the logs per second.
