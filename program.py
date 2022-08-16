from asyncio.windows_events import NULL

car = ['null', False, False]
carA = 0

van = ['null', False, False]
vanA = 0

treeWheel = ['null', False]
treeWheelA = 0 

truck = ['null', 'null', False, False]
truckA = 0
truckB = 0

lorry = ['null', 'null', False, False]
lorryA = 0
lorryB = 0

isLoop = True
option = NULL

def selected (name) :
    print("\nYou selected: " + name)
    print("\nVehicle booking successful")
    input("\nPress ENTER to complete the hire...")
    print("\n....................................................................")
    print("\nHire completed successfully...")

def startOptions () :
    print("""
....................................................................

    *** Welcome to Cab Service ***

    Options ->

            a - Add a vehicle
            r - Remove a vehicle
            m - Make a hire
            s - See available vehicles

            PRESS ENTER KEY TO EXIT

....................................................................
    """)
    global option
    option = input("Enter your option --> ").lower().strip()
   


def addVehicle () :
    global option, car, van, treeWheel, truck, lorry, carA, vanA, treeWheelA, truckA, truckB, lorryA, lorryB
    if option == 'a' :
            print("""
....................................................................

                *** Add a vehicle ***

                Vehicle Types ->

                        c - Car
                        v - Van
                        w - 3 Wheelers
                        t - Truck
                        l - Lorry

                        PRESS ENTER KEY TO RETURN TO MAIN

....................................................................
            """)
            type = input("Enter your option --> ").lower().strip()
            if type == 'c' :
                carA =  carA + 1
                print("\nYour vehicle added successfully")
            
            elif type == 'v' :
                vanA =  vanA + 1
                print("\nYour vehicle added successfully")

            elif type == 'w' :
                treeWheelA =  treeWheelA + 1
                print("\nYour vehicle added successfully")

            elif type == 't' :
                print("""
....................................................................

            Truck Types ->

                    a - 7 ft
                    b - 12 ft

                   PRESS ENTER KEY TO RETURN TO MAIN      

....................................................................
            """)
                subType = input("Enter Your Option --> ").lower().strip()
                if subType == 'a' :
                    truckA =  truckA + 1
                    print("\nYour vehicle added successfully")
                elif subType == 'b' :
                    truckB =  truckB + 1
                    print("\nYour vehicle added successfully")

            elif type == 'l' :
                print("""
....................................................................

            Lorry Types ->

                    a - 2500kg
                    b - 3500kg

                   PRESS ENTER KEY TO RETURN TO MAIN      

....................................................................
            """)
                subType = input("Enter Your Option --> ").lower().strip()
                if subType == 'a' :
                    lorryA =  lorryA + 1
                    print("\nYour vehicle added successfully")
                elif subType == 'b' :
                    lorryB =  lorryB + 1
                    print("\nYour vehicle added successfully")
            else :
                print("\nVehicle adding unsuccessful")

def removeVehicle () :
    global option, car, van, treeWheel, truck, lorry, carA, vanA, treeWheelA, truckA, truckB, lorryA, lorryB
    if option == 'r' :
            print("""
....................................................................

                *** Remove a vehicle ***

                Vehicle Types ->

                        c - Car
                        v - Van
                        w - 3 Wheelers
                        t - Truck
                        l - Lorry

                        PRESS ENTER KEY TO RETURN TO MAIN

....................................................................
            """)
            type = input("Enter your option --> ").lower().strip()
            if type == 'c' :
                if carA == 0 :
                    print("There are no vehicles to remove...")
                else :
                    carA = carA - 1
                    print("\nYour vehicle removed successfully")
            
            elif type == 'v' :
                if vanA == 0 :
                    print("There are no vehicles to remove...")
                else :
                    vanA = vanA - 1
                    print("\nYour vehicle removed successfully")

            elif type == 'w' :
                if treeWheelA == 0 :
                    print("There are no vehicles to remove...")
                else :
                    treeWheelA = treeWheelA - 1
                    print("\nYour vehicle removed successfully")

            elif type == 't' :
                print("""
....................................................................

            Truck Types ->

                    a - 7 ft
                    b - 12 ft

                   PRESS ENTER KEY TO RETURN TO MAIN      

....................................................................
            """)
                subType = input("Enter Your Option --> ").lower().strip()
                if subType == 'a' :
                    if truckA == 0 :
                        print("There are no vehicles to remove...")
                    else :
                        truckA = truckA - 1
                        print("\nYour vehicle removed successfully")
                elif subType == 'b' :
                    if truckB == 0 :
                        print("There are no vehicles to remove...")
                    else :
                        truckB = truckB - 1
                        print("\nYour vehicle removed successfully")

            elif type == 'l' :
                print("""
....................................................................

            Lorry Types ->

                    a - 2500kg
                    b - 3500kg

                   PRESS ENTER KEY TO RETURN TO MAIN      

....................................................................
            """)
                subType = input("Enter Your Option --> ").lower().strip()
                if subType == 'a' :
                    if lorryA == 0 :
                        print("There are no vehicles to remove...")
                    else :
                        lorryA = lorryA - 1
                        print("\nYour vehicle removed successfully")
                elif subType == 'b' :
                    if lorryB == 0 :
                        print("There are no vehicles to remove...")
                    else :
                        lorryB = lorryB - 1
                        print("\nYour vehicle removed successfully")
            else :
                print("\nVehicle removing unsuccessful")

def availableVehicles () :
    global option, car, van, treeWheel, truck, lorry
    if option == 's' :
        print("....................................................................")
        print("*** Available vehicles ***")
        print("\nCars: " + str(carA))
        print("Vans: " + str(vanA))
        print("3 Wheelers: " + str(treeWheelA))
        print("Trucks: ")
        print("     7 ft Trucks: " + str(truckA))
        print("     12 ft Trucks: " + str(truckB))
        print("Lorries: ")
        print("     2500kg Lorries: " + str(lorryA))
        print("     3500kg Lorries: " + str(lorryB))
        print("\n....................................................................")

        input("\nEnter any key to return to main --> ")

def makeHire () :
    global car, van, treeWheel, lorry, truck, carA, vanA, treeWheelA, truckA, truckB, lorryA, lorryB
    if option == 'm' :
        print("""
....................................................................

                *** Make a hire ***

                Hire Types ->

                        p - Travel for passengers
                        l - Carry payloads
                        t - Trucks
                
                        PRESS ENTER KEY TO RETURN TO MAIN 

....................................................................
        """)
            
        subOption = input("Enter your option --> ").lower().strip()

        if subOption == 'p' :
            print("\n....................................................................")
            print("\nYou selected: Travel for passengers")
            print("\n....................................................................")
            if carA > 0 or vanA > 0 or treeWheelA > 0 :   
                noPassengers = input("\nNumber of passengers(Max: 8) --> ")
                status = noPassengers.isdigit()

                if status :
                    if carA > 0 :
                        if int(noPassengers) <= 3 :
                            car[1] = True
                        if int(noPassengers) <= 4 :
                            car[2] = True

                    if vanA > 0 :
                        if int(noPassengers) <= 6 :
                            van[1] = True
                        if int(noPassengers) <= 8 :
                            van[2] = True
                            
                    if treeWheelA > 0 :
                        if int(noPassengers) <= 3 :
                            treeWheel[1] = True

                    print("\n....................................................................")
                    print("\nAvailable vehicles: ")
                    if car[2] :
                        print("\na - Car(Non-AC)")
                    if car[1] :
                        print("b - Car(AC)")
                    if van[2] :
                        print("c - Van(Non-AC)")
                    if van[1] :
                        print("d - Van(AC)")
                    if treeWheel[1] :
                        print("e - 3 Wheeler")
                    if not car[2] and not car[1] and not van[2] and not van[1] and not treeWheel[1] :
                        print("\nNo vehicles available at the moment...")
                    print("\nPRESS ENTER KEY TO RETURN TO MAIN")
                    print("\n....................................................................")

                    select = input("\nSelect your vehicle --> ").lower().strip()
                    if select == 'a' and car[2] :
                        carA = carA - 1
                        selected("Non-AC Car")
                        carA = carA + 1
                    elif select == 'b' and car[1] :
                        carA = carA - 1
                        selected("AC Car")
                        carA = carA + 1
                    elif select == 'c' and van[2] :
                        vanA = vanA - 1
                        selected("Non-AC Van", vanA)
                        vanA = vanA + 1
                    elif select == 'd' and van[1] :
                        vanA = vanA - 1
                        selected("AC Van")
                        vanA = vanA + 1
                    elif select == 'e' and treeWheel[1] :
                        treeWheelA = treeWheelA - 1
                        selected("3 Wheeler")
                        treeWheelA = treeWheelA + 1
                else :
                    print("\nInvalid value")
            else :
                print("\nNo vehicles available at the moment...")    
            car[1] = False
            car[2] = False
            van[1] = False
            van[2] = False
            treeWheel[1] = False    
                
        if subOption == 'l' :
            print("\n....................................................................")
            print("\nYou selected: Carry payloads")
            print("\n....................................................................")

            if lorryA > 0 or lorryB > 0 :
                weight = input("\nWeight of payload(kg) (Max: 3500) --> ")
                status = weight.isnumeric()

                if status :
                    if lorryA > 0 :
                        if int(weight) <= 2500 :
                            lorry[2] = True
                    elif lorryB > 0 :
                        if int(weight) <= 3500 :
                            lorry[3] = True

                    print("\n....................................................................")
                    print("\nAvailable vehicles: ")
                    if lorry[2] :
                        print("\na - Lorry(2500kg)")
                    if lorry[3] :
                        print("b - Lorry(3500kg)")
                    if not lorry[2] and not lorry[3] :
                        print("\nNo vehicles available at the moment...")
                    print("\nPRESS ENTER KEY TO RETURN TO MAIN")
                    print("\n....................................................................")

                    select = input("\nSelect your vehicle --> ").lower().strip()
                    if select == 'a' and lorry[2] :
                        lorryA = lorryA - 1
                        selected("Lorry(2500kg)")
                        lorryA = lorryA + 1
                    elif select == 'b' and lorry[3] :
                        lorryB = lorryB - 1
                        selected("Lorry(3500kg)")
                        lorryB = lorryB + 1
                else :
                    print("\nInvalid value")
            else :
                print("\nNo vehicles available at the moment...")
            lorry[2] = False
            lorry[3] = False

        if subOption == 't' :
            print("\n....................................................................")
            print("\nYou selected: Trucks")
            print("\n....................................................................")

            if truckA > 0 or truckB > 0 :
                length = input("Length of payload(ft) --> ")

                status = length.isnumeric()

                if status :
                    if truckA > 0 :
                        if int(length) <= 7 :
                            truck[2] = True
                    elif truckB > 0 :
                        if int(length) <= 12 :
                            truck[3] = True

                    print("\n....................................................................")
                    print("\nAvailable vehicles: ")
                    if truck[2] :
                        print("\na - Truck(7 ft)")
                    if truck[3] :
                        print("b - Truck(12 ft)")
                    if not truck[2] and not truck[3] :
                        print("\nNo vehicles available at the moment...")
                    print("\nPRESS ENTER KEY TO RETURN TO MAIN")
                    print("\n....................................................................")

                    select = input("\nSelect your vehicle --> ").lower().strip()
                    if select == 'a' and truck[2] :
                        truckA = truckA - 1
                        selected("Truck(7 ft)")
                        truckA = truckA + 1
                    elif select == 'b' and truck[3] :
                        truckB = truckB - 1
                        selected("Truck(12 ft)")
                        truckB = truckB + 1
                else :
                    print("\nInvalid value")
            else :
                print("\nNo vehicles available at the moment...")
            truck[2] = False
            truck[3] = False


def exit () :
    global isLoop, option
    if not option == 'a' and not option == 'r' and not option == 'm' and not option == 'c' and not option == 's' :
        isLoop = False
        print("\n*** Closed ***")


while isLoop :
    startOptions()
    addVehicle()
    removeVehicle()
    makeHire()
    availableVehicles()
    exit()
 