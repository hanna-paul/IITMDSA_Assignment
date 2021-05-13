import mysql.connector
class student:
    def __init__(self):
        connection= mysql.connector.connect(host="localhost",user="root",password="")
        cursor=connection.cursor()
        sql="create database if not exists learning"
        cursor.execute(sql)
        print("Database created successfully..")
        cursor=connection.cursor()
        cursor.execute("Use learning")
        query="create table if not exists Student \
               (Std_ID int primary key,\
                Name varchar(20) not null,\
                Dept varchar(15),\
                Sub1 int,Sub2 int,Sub3 int,Sub4 int,Sub5 int,\
                Total int,Average float,Grade varchar(10))"
        print("Table Student created successfully..")
        cursor.execute(query)
        

            
    def input(self):
        ID=int(input("Enter the ID: "))
        name_1=input("Enter the name of the student: ")
        Dept=input("Enter the department: ")
        Sub1=int(input("Mark of Sub1: "))
        Sub2=int(input("Mark of Sub2: "))
        Sub3=int(input("Mark of Sub3: "))
        Sub4=int(input("Mark of Sub4: "))
        Sub5=int(input("Mark of Sub5: "))
        

        self.total=self.get_total(Sub1,Sub2,Sub3,Sub4,Sub5)
        self.avg=self.get_avg(self.total)
        self.grade=self.get_grade(self.avg)
        
        connection=mysql.connector.connect(host="localhost",user="root",password="",database="learning")
        cursor=connection.cursor()
        # query1="insert into Student(Std_ID,Name,Dept,Sub1,Sub2,\
        #         Sub3,Sub4,Sub5,Total,Average,Grade)\
        #         values({},{},{},{},{},{},{},{},{},{},{})".format(ID,name_1,Dept,Sub1,Sub2,\
        #                                                                              Sub3,Sub4,Sub5,self.total,self.avg,self.grade)
        
        query="insert into Student(Std_ID,Name,Dept,Sub1,Sub2,\
                Sub3,Sub4,Sub5,Total,Average,Grade)\
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
        val = (ID,name_1,Dept,Sub1,Sub2,Sub3,Sub4,Sub5,self.total,self.avg,self.grade)
        
        cursor.execute(query,val)
        connection.commit()     
               
    def get_total(self,Sub1,Sub2,Sub3,Sub4,Sub5):
        sum=Sub1+Sub2+Sub3+Sub4+Sub5
        return sum
    
    def get_avg(self,Total):
        avg=(self.total)/5
        return avg

    def get_grade(self,avg):
        if avg>=90:
            grade="A"
        elif avg>=80 and avg<90:
            grade="B"
        elif avg>=70 and avg<80:
            grade="C"
        elif avg>=60 and avg<70:
            grade="D"
        elif avg>=40 and avg<60:
            grade="E"
        else:
            grade="F"
        return grade

student_obj=student()
student_obj.input()
