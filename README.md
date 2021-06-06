# Temperature prediction algorithm v1.0.1 - CookSense
**Note: This project has three parts, Data Visualisation, Data Collection and Server creation**
```diff
+ Update: Friday, June 6 - 08:54 IST
+ Completion of phase 1
+ v1.0.1 with analytics and data in Repository
+ Seamless updation and email notification and analytics
+ Creation of Email Notification complete
```
## **Note: The project is still under construction. Hopefuly you can understand a little bit from the idea of the readme**
## The Project
### CookSense_v1.0.0
- In its current form the project can collect data and upload to thingspeak.
- This data can be processed once the data is saved.
- The saved data can be used for visualisation.
- **There will be 10 updates from v1.0.0 to v1.0.9 with hardware improvements and increments to the code accordingly.**
- **The initial marketable product shall be CookSense v1.1.0a and v1.1.0b**
```diff
- For CookSense v1.0.2: Better analytics and collection of more data
```

## Data processing and visualisation
### Directions of use
- Clone the library to your System.
- Run pip to install requirements that are necessary, **It is recommended to have anaconda installed on your system**
- Run the iPython Notebook on jupyter lab
- Requirements
  - Turicreate
  - Datetime
  - Numpy
  - Matplotlib.pyplot

## Using the ESP8266 for data collection with thingspeak
### Directions of use
- Create a simple Temperature sensor using two sensors.
  - A probe type temperature
  - An Ambient Temperature sensor
- Use the arduino IDE to collect data and send the data to thingspeak using API
- Export the code from thingspeak

```diff
- Pending: Create server
+ Complete: Basic MVP for Class project purposes.

! Direction Forward:
! Better analytics
! Better preprocessing.
```
