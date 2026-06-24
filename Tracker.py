print("Hello, friend!")

track_vehicle = input("Did you use your vehicle today? (Yes/No) " )
if track_vehicle == "Yes" or track_vehicle == "yes" or track_vehicle == "Y" or track_vehicle == "y":
    vehicle_miles = float(input("Roughly how many miles did you drive today? "))
    vehicle_emissions = vehicle_miles * 0.4
    print ("Your vehicle emissions today:", round(vehicle_emissions, 2), "kg of CO2")
else:
    vehicle_emissions = 0
    print ("You should go out more.")

track_public = input("Did you use public transport today? (Yes/No) " )
if track_public == "Yes" or track_public == "yes" or track_public == "Y" or track_public == "y":
    public_miles = float(input("Roughly how many miles did you travel via public transport today? "))
    public_emissions = public_miles * 0.1
    print ("Your public transport emissions today:", round(public_emissions, 2), "kg of CO2")
else:
    public_emissions = 0
    print ("Not a fan, I assume?")

track_electricity = input("Did you use some electricity today? (Yes/No) " )
if track_electricity == "Yes" or track_electricity == "yes" or track_electricity == "Y" or track_electricity == "y":
    electricity_kwh = float(input("Roughly how many kWh of electricity did you use today? "))
    electricity_emissions = electricity_kwh * 0.2
    print ("Your electricity emissions today:", round(electricity_emissions, 2), "kg of CO2")
else:
    electricity_emissions = 0
    print ("Cosplaying a caveman, I see..." )

total_emissions = vehicle_emissions + electricity_emissions + public_emissions
print ("Your TOTAL emissions today:", round(total_emissions, 2), "kg of CO2")