# script for purchasing a car
cars={'Toyota Camry':450000,'Honda Civic':600000,'Nissan Patrol':870000,'Ford Mustang':567000,'BMW 3 Series':44500,\
      'Chevrolet Camaro':456700,'Mercedes-Benz C-Class':768000,'Audi A4':533770,'Hyundai Elantra':768000,'Kia Optima':875409,\
          'Mazda3':890788,'Volkswagen Jetta':764002,'Subaru Impreza':889900,'Lexus ES':1000000,'Porsche 911':1230000,'Ferrari 488':3210000,\
              'lamborghini Aventador':8800000,'McLaren 720S':5600000,'Tesla Model S':778000,'Jeep Wrangler':545000,'Dodge Charger':90000,\
                  'GMC Sierra':689000,'Cadillac ATS':666000,'Buick Enclave':745000,'Volvo S60':978000,'Bentley Continental':900000,'Range Rover Sport':887000,\
                      'Rolls Royce Ghost':5000000,'Chrysler Minivian': 453000,'Infiniti Q50':890000}
#prompt user to enter car name
carBrand=input('Enter car brand: ')
#check whether the car brand is available in the list of cars available
if carBrand in cars:
    print('YES,%s is available'%(carBrand))
    print('The price is $',cars[carBrand])
else:
    print('NO, Car is not available')