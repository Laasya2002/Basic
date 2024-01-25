def main(inparam1):
    def inn(inparam2):
        def inn2(inparam3):
            def inn3(inparam4):
                return inparam1+inparam2+inparam3+inparam4
            return inn3
        return inn2
    return inn
if __name__=="__main__":
    inval=int(input("Enter the inval: "))
    directed_value=main(inval)
    inval2=int(input("Enter the inval2: "))
    x=directed_value(inval2)
    inval3=int(input("Enter the inval3: "))
    y=x(inval3)
    inval4=int(input("Enter the inval4: "))
    print(y(inval4))
