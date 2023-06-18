name = str(input("Enter Student's Name: "))
stuid = int(input("Enter Student's Number: "))
fsub = str(input("Enter Subject 1 name: "))
fmid = float(input("Enter Midterm Grade for " + fsub + ": "))
ffin = float(input("Enter Final Grade for " + fsub + ": "))

ssub = str(input("Enter Subject 2 name: "))
smid = float(input("Enter Midterm Grade for " + ssub + ": "))
sfin = float(input("Enter Final Grade for " + ssub + ": "))

fnsub = str(input("Enter Subject 3 name: "))
fnmid = float(input("Enter Midterm Grade for " + fnsub + ": "))
fnfin = float(input("Enter Final Grade for " + fnsub + ": "))

print("\nGRADE OVERVIEW: ---------------------------------\n")

print("Student's Name: " + name)
print("Student's Number: " + str(stuid))

fave = (fmid + ffin) / 2
save = (smid + sfin) / 2
fnave = (fnmid + fnfin) / 2

if fave > 70:
    fverd = "Passed"
else:
    fverd = "Failed"

if save > 70:
    sverd = "Passed"
else:
    sverd = "Failed"

if fnave > 70:
    fnverd = "Passed"
else:
    fnverd = "Failed"

print(fsub + ": " + str(fave) + "% -- " + fverd)
print(ssub + ": " + str(save) + "% -- " + sverd)
print(fnsub + ": " + str(fnave) + "% -- " + fnverd) 

tave = (fave + save + fnave) / 3
if tave > 70:
    ffverd = "Passed"
else:
    ffverd = "Failed"

print("Total Average: " + str(tave) + "%")
print("Remarks: " + ffverd)