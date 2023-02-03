kata = (0, 4, 132.42222, 10000, 12345.67)
str1 = f"module_{kata[0]:02d}"
str2 = f"ex_{kata[1]:02d}"
str3 = f"ex_{round(kata[2], 2)}"
str4 = "{:.2e}".format(kata[3])
str5 = "{:.2e}".format(kata[4])
print(str1 + ",", str2 , ":", str3 + ",", str4 +  ",", str5)