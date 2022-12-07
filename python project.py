# Creating Multiplication Table using Object Oriented programming
class table:
    def tab(self):
        n=int(input("Enter a no.: "))
        for i in range(2,n+1):
            for j in range (1,11):
                print(i,'*',j,'=', i*j)


a=table()
a.tab()


