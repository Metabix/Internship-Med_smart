# Med_smart
Installation
Reboot sd card
Flash backup_SDcard.img to the sd card wait time 35 min
After flashing, enter the wpa_supplicant and ssh file, with the wlan credentials
Open putty and enter the ip address of the pi
Sudo apt-get upgrade
Sudo apt-get update
Sudo apt-get install xrdp
Open remote desktop
Enter the ip address
Access temp&gt;electron..&gt;python&gt;mqtt...py
Change the mqtt ip address to the raspberry pi’s address

Open arduino IDE;
In the program given:
Change the mqtt ip address to the raspberry pi
Change the wifi credentials as well
Upload

Testing

Check the arduino serial monitor
See if mqtt connection is established
Check the temperature readings and whether the message is being pushed
Also check if motor is working
Open remote desktop
Access the dbms and check for the data stored

Sudo mysql -u root -p
Password : admin
USE MEDSMART
Select * from Userdat; // displays the data ;
If there is some data type “TRUNCATE TABLE Userdat;”
Select * from Userdat; // displays the data ;
Exit // to exit

Installation

Find the wifi id and password of the client’s network;
Add it in the wpa_supplicant file in raspberry pi

Get the ip address of the raspberry pi and update it in the mqtt.py code in place
of the old ip address
Similarly update the wifi id and password for the esp and update the mqtt
address.
