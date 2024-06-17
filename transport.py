import mysql.connector
from tabulate import tabulate
con = mysql.connector.connect(
   user='root', password='', host='localhost', database='project')
cursor = con.cursor()
def Admin():
      def assignment():
            print("Assignment Details:")
            query2="select * from assignments"
            cursor.execute(query2)
            table=cursor.fetchall()
            headers=["Driver Name","Vehicle Id","Route Id","Date"]
            print(tabulate(table, headers=headers, tablefmt="psql"))
      def changevehicle():
            name=input("Enter Name Of The Car: ")
            price=input("Price: ")
            avail=input("Availability: ")
            query1="INSERT INTO vehicles(name, price,availability) VALUES (%s,%s,%s)"
            cursor.execute(query1,(name,price,avail))
            con.commit()
            print("Successfully Inserted")
            vehicles()
      def changedrivers():
            name=input("Enter Name Of The Car: ")
            id=input("Driver Id: ")
            license=input("License: ")
            mobile=input("Enter Mobile: ")
            query1="INSERT INTO drivers(name, driver_id,license_number,mobile) VALUES (%s,%s,%s,%s)"
            cursor.execute(query1,(name,id,license,mobile))
            con.commit()
            print("Successfully Inserted")
            drivers()
      def changeroutes():
            Routeid=input("Enter Route Id: ")
            pickup=input("Enter Pickup Point: ")
            drop=input("Enter Drop Point: ")
            dist=input("Enter Distance From Starting Location to Destination: ")
            query1="INSERT INTO routes(route_id,startloc,endloc,distance) VALUES (%s,%s,%s,%s)"
            cursor.execute(query1,(Routeid,pickup,drop,dist))
            con.commit()
            print("Successfully Inserted")
            routes()
      def changetransport():
            Vid=input("Enter Vehicle Id: ")
            numberplate=input("Enter Plate Number: ")
            license=input("Enter Name: ")
            mobile=input("Enter Model: ")
            capacity=input("Enter Capacity: ")
            query1="INSERT INTO transport(vehicle_id,license_plate,Name,model,capacity) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query1,(Vid,numberplate,license,mobile,capacity))
            con.commit()
            print("Successfully Inserted")
            transport()
      def deletevehicle():
            name=input("Enter Name Of The Car: ")
            query1="DELETE FROM vehicles WHERE name=%s"
            adr=(name,)
            cursor.execute(query1,adr)
            con.commit()
            print("Successfully Deleted")
            vehicles()
      def deletedrivers():
            name=input("Enter Name Of The Car: ")
            query1="DELETE FROM drivers WHERE name=%s"
            adr=(name,)
            cursor.execute(query1,adr)
            con.commit()
            print("Successfully Deleted")
            drivers()
      def deleteroutes():
            Routeid=input("Enter Route Id: ")
            query1="DELETE FROM routes WHERE Route_id=%s"
            adr=(Routeid,)
            cursor.execute(query1,adr)
            con.commit()
            print("Successfully Deleted")
            routes()
      def deletetransport():
            vehicleid=input("Enter Route Id: ")
            query1="DELETE FROM transport WHERE vehicle_id=%s"
            adr=(vehicleid,)
            cursor.execute(query1,adr)
            con.commit()
            print("Successfully Deleted")
            transport()
      ad=input("1.Insert Details\n2.Delete Details\n3.Add Assignments To Drivers\n")
      if ad=='1':
            def insertdetails():
                  print("1.vehicle Datails\n2.Driver Details\n3.Route Details\n4.Transport Details5.Logout")
                  choice=input("Enter Choice for Inserting the details")
                  if choice=='1':
                        changevehicle()
                  elif choice=='2':
                        changedrivers()
                  elif choice=='3':
                        changeroutes()
                  elif choice=='4':
                        changetransport()
                  else:
                        print("Enter Valid Choice")
            insertdetails()
      elif ad=='2':
            def deletedetails():
                  print("1.vehicle Datails\n2.Driver Details\n3.Route Details\n4.Transport Details")
                  choice=input("Enter Choice for Deleting the details")
                  if choice=='1':
                        deletevehicle()
                  elif choice=='2':
                        deletedrivers()
                  elif choice=='3':
                        deleteroutes()
                  elif choice=='4':
                        deletetransport()
                  else:
                        print("Enter Valid Choice")
            deletedetails()
      elif ad=='3':
            def assignments():
                  drivername=input("Enter Name of the Driver")
                  vehicleid=input("Enter Vehicle Id")
                  routeid=input("Enter Route Id")
                  date=input("Enter Date of Assignment")
                  query1="INSERT INTO assignments(drivername,vehicleid,routeid,date) VALUES (%s,%s,%s,%s)"
                  cursor.execute(query1,(drivername,vehicleid,routeid,date))
                  con.commit()
                  print("Assignment Successfully Assigned")
                  assignment()
            assignments()
def vehicles():
      print("Vehicles: ")
      query1="select * from vehicles"
      cursor.execute(query1)
      table=cursor.fetchall()
      headers = ["Name","Price","Availability"]
      print(tabulate(table, headers=headers, tablefmt="psql"))
def drivers():
      print("Vehicles Details:")
      query2="select * from drivers"
      cursor.execute(query2)
      table=cursor.fetchall()
      headers=["Name","Driver Id","License Number","Mobile No"]
      print(tabulate(table, headers=headers, tablefmt="psql"))
def  routes():
      print("Routes:")
      query2="select * from routes"
      cursor.execute(query2)
      table=cursor.fetchall()
      headers=["Route ID","Start Location","Destination","Distane in KM"]
      print(tabulate(table, headers=headers, tablefmt="psql"))
def  transport():
      print("Transport Details:")
      query2="select * from transport"
      cursor.execute(query2)
      table=cursor.fetchall()
      headers=["Vehicle Id","License Plate","Name","Model","Capacity"]
      print(tabulate(table, headers=headers, tablefmt="psql"))
def check():
    print("\n\033[1mWelcome!!\033[0m")
    brand=input("Car Name:")
    availability="A"
    query="SELECT * FROM vehicles WHERE name=%s and availability=%s"
    cursor.execute(query,(brand,availability))
    found=cursor.fetchall()
    if found:
        print("\n\033[1mAvailable!!\033[0m")
    else:
        print("\n\033[1mNot Available!!\033[0m")
def payment():
      carname=input("Enter Car Name")
      query1='SELECT price FROM vehicles WHERE name = %s'
      cursor.execute(query1,(carname,))
      result=cursor.fetchone()
      if result:
            print(f"The price of for 25KM is{carname} is {result[0]}")
      x=input("Enter PickupZone")
      y=input("Enter DropZone")
      dist=int(input("Enter Distance From StartZone To endZone"))
      r=int(result[0])
      amount=r*dist
      print("Transport Charges For You Trip : ",amount)
def booking():
      n=input("Enter Your Name")
      vn=input("Enter Vehicle Name")
      m=input("Enter Mobile Number")
      print("Enter Amount")
      query1='SELECT price FROM vehicles WHERE name = %s'
      cursor.execute(query1,(vn,))
      result=cursor.fetchone()
      if result:
            print(f"The price of {vn} for 25KM  is {result[0]}")
      x=input("Enter PickupZone")
      y=input("Enter DropZone")
      dist=int(input("Enter Distance From StartZone To endZone"))
      r=int(result[0])
      amount=r*dist
      print("Transport Charges For You Trip : ",amount)
      td=input("Enter Trip Date")
      query1="INSERT INTO trips(customer_name,vehicle_name,mobileno,amount,tripdate) VALUES (%s,%s,%s,%s,%s)"
      cursor.execute(query1,(n,vn,m,amount,td))
      con.commit()
      print("Successfully Booked")
def customer():
      flag=0
      while(flag==0):
            print("1.Vehicles And Their Price for 25 KiloMetes\n2.Check Availability\n3.Transport Details\n4.Payments Details\n5.Booking\n\033[1m or Exit customer\033[0m\n")
            choice=int(input("Enter Your Choice"))
            if choice==1:
                  vehicles()
            elif choice==2:
                  check()
            elif choice==3:
                  transport()
            elif choice==4:
                  payment()
            elif choice==5:
                  booking()
            else:
                  flag=1

def main():
      print("-"*50,"SR Transport Management System","-"*50)
      print("1.Admin\n2.Customer")
      x=input("Enter your Choice:")
      if x=='1':
            Admin()
      else:
            customer()
vehicles()
drivers()
transport()
routes()
main()