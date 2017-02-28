import pyowm

owm = pyowm.OWM('c9b216773fc03af4d001dd748f51d31a')  
observation = owm.weather_at_place("London,uk")  
w = observation.get_weather()  
temperature = w.get_temperature('celsius')  
tomorrow = pyowm.timeutils.tomorrow()  
wind = w.get_wind()  
print ("w")
print(w)  
print("wind")
print(wind)  
print(temperature)  
print(tomorrow) 
