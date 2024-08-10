marks = int(input("student marks"))
if marks >= 90:
    print("A grade")
else:
    if marks >= 80:
     print("B grade")
    else:                          #can use elif statements
      if marks >=70:
        print("C grade")
      else:
        if marks >= 60:
            print("D grade")
        else:    print(" Fail")