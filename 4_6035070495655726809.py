#Cars and their sales prices
Cars=['Toyota,Mercedes-Benz,Suzuki,Honda,Hyundai,Lexus,Jeep,Kia,Ford,Chevrolet,GMC,BMW,Dodge,Range Rover,Nissan']
Toyota={'TOYOTA Corolla':'GHC 110,000','TOYOTA RAV4':'GHC 301,000','TOYOTA yaris':'GHC 201,000','TOYOTA Highlander':'803,000','TOYOTA Prado':'GHC 602,000'}
MercedesBenz={'Mercedes-Benz AMG C43':'GHC 590,900','Mercedes-Benz AMG C63':'GHC 870,100','Mercedes-Benz AMG CLA35':'GHC 495,000'}
Suzuki={'Suzuki Alto 800':'GHC 450,440','Suzuki swift 1.2 MT':'GHC 560,662','Suzuki Jimny JX MT':'GHC 570,011'}
Honda={'Honda CR-V':'GHC 386,889','Honda Civic':'GHC 450,556','Honda HR-V':'GHC 455,996','Honda Accord':'GHC 321,100'}
Hyundai={'Hyundai Elantra':'GHC 206,500','Hyundai IONIQ 5':'GHC 414,500','Hyundai Sonata':'GHC 245,500'}
Lexus={'Lexus ES250':'GHC 414,400','Lexus ES300h':'GHC 426,400','Lexus GX460':'GHC 564,250'}
jeep={'Grand Cherokee':'GHC 324,440','Wrangler 4xe':'GHC 335,560','Compass':'GHC 430,230'}
Kia={'Kia Forte':'GHC 196,900','Kia Rio':'GHC 167,500','Kia EV6':'487,000'}
Ford={'EcoSport':'GHC 220,400','Escape':'GHC 275,000','Bronco Sport':'GHC 292,150'}
Chevrolet={'Chevrolet Camaro':'GHC 264,000','Chevrolet Corvette':'GHC 645,000','Chevrolet Blazer':'GHC 351,000'}
GMC={'GMC Acardia':'GHC 368,000','GMC Yukon':'GHC 574,000','GMC Canyon':'GHC 369,000','GMC HUMMER EV':'GHC 1,087,000'}
BMW={'BMW ALPINA XB7':'GHC 1,450,000','BMW X1':'GHC 391,000','BMW 330':'GHC 438,000'}
Dodge={'Dodge Challenger':'GHC 305,450','Dodge Charger':'GHC 326,450','Dodge Durango':'GHC 384,950'}
Nissan={'Nissan Altima':'GHC 252,900','Nissan GT-R':'GHC 1,135,4000','Nissan Maxima':'GHC 381,400'}

Car_type= input('which car do you want: ')
Car_type= Car_type.title()
if Car_type == 'Toyota':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Toyota)
if Car_type == 'MercedesBenz':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(MercedesBenz)
if Car_type == 'Suzuki':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Suzuki)
if Car_type == 'Honda':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Honda)    
if Car_type == 'Hyundai':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Hyundai)    
if Car_type == 'Lexus':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Lexus)
if Car_type == 'Jeep':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(jeep)
if Car_type == 'Kia':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Kia)    
if Car_type == 'Ford':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Ford)
if Car_type == 'Chevrolet':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Chevrolet)
if Car_type == 'GMC':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(GMC)
if Car_type == 'BMW':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(BMW)
if Car_type == 'Dodge':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Dodge)
elif Car_type == 'Nissan':
    print('these are the available brands of ' + Car_type  + 'with their respective prices')
    print(Nissan)    
    
#https://github.com/laud-antwi/Data-Structures-    