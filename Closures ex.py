from math import factorial
def main():
    print("You are in the main function")
    y=10#local scope for main()
    def inner():
        print("You are in the inner scope")
        x=factorial(5)
        print(y)#enclosing scope
        return x
    return inner
if __name__=="__main__":
    x=main()
    print(x())
    
