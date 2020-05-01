import openpyxl
import datetime

nl = "\n"
pattern1 = "------------------------------------------"
pattern2 = "*******************************************"

wb = openpyxl.load_workbook("C:\\Users\\...readings_new.xlsx")
sheet = wb.active
a = sheet.columns
w = []
for item in a:
    w.append(item)                                                                  # all data is appended into a list
                                                                                    # data is taken from columns
sujith_pre = w[1][-1].value                                                   # accessing the data
ram_pre = w[2][-1].value
amt = w[3][-1].value
date = str(datetime.date.today())
date1 = str(datetime.datetime.now())                              # datetime module using

bill = int(input("Bill amount : "))
unit_pre = ram_pre
unit_cur = int(input("Current downstairs bill units : "))
up_pre = sujith_pre
up_cur = float(input("Current upstairs units : "))

tot_unit = unit_cur - unit_pre                                          # calculations
up_unit = up_cur - up_pre
rpu = bill / tot_unit
down_unit = tot_unit - up_unit

print(pattern1)
print(date1.center(42,"*"))
print(pattern1)
print("Rate per unit : ", rpu, "INR")
print(pattern1)


print("Downstairs units used : ", down_unit)
print("Downstairs amount payable : ", down_unit*rpu, "INR")

print(pattern2)

print("Upstairs units used : ", up_unit)
print("Upstairs amount payable : ", up_unit*rpu, "INR")

# ADDING DATA AND SAVING IT
sheet.append([date,up_cur,unit_cur,bill])                                            # Adding data
wb.save("C:\\Users\\...readings_new.xlsx")                                          # Saving data


outFilename = "C:\\Users\\"+str(date)+".txt"                         #create a .txt file in the location with file name as date
outFilename = open(outFilename,"w+")
outFilename.write("""
Bill amount : """ + str(bill) + nl +"""
Previous bill units : """+str(ram_pre)+ nl+"""
Current bill units : """+str(unit_cur)+nl+"""
Previous upstairs units : """+str(sujith_pre)+nl+"""
Current upstairs units : """+str(up_cur)+nl+"""
------------------------------------------
Rate per unit : """+str(rpu)+""" INR
------------------------------------------
Downstairs units used : """+str(down_unit)+nl+"""
Downstairs amount payable :  """+str(down_unit*rpu)+""" INR
*******************************************
Upstairs units used :  """+ str(up_unit)+nl+"""
Upstairs amount payable :  """+str(up_unit*rpu)+ """INR

""")                                                            #inside {line 54} outFilename.write("...") is the format I need while saving the text document
outFilename.close()                                             #and the data in """ """ is multiline data
