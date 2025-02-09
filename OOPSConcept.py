class ConceptofOOPS():
     def Subfields():
         print("Sub-fields in AI are:")
         list1=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
         for Subfield in list1:
            print(Subfield)
     def OddEven(num):
         return num%2
     def eligible(gender,age):
        if(gender.upper()=="MALE" and age >=21):
            message="ElIGIBLE"
        elif(gender.upper()=="FEMALE" and age >=18):
            message="ElIGIBLE"
        else:
            message="NOT ElIGIBLE"
        return message
    def percentage(sub1,sub2,sub3,sub4,sub5):
        print(f"Total:{sub1+sub2+sub3+sub4+sub5}")
        return (sub1+sub2+sub3+sub4+sub5)/5
    def area(height,breadth):
        print("Area formula: (Height*Breadth)/2")
        return (height*breadth)/2
    def perimeter(h1,h2,b1):
        print("Perimeter formula: Height1+Height2+Breadth")
        return h1+h2+b1
    