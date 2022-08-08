onlineShop = {
 "keychain":"0.75$",
 "t-shirt":"8.50$",
 "bottle":"10.0$"
}
#print(onlineShop)
#print(onlineShop["The bottle is ","bottle"])

keychain=onlineShop["keychain"]
tshirt=onlineShop["t-shirt"]
bottle=onlineShop["bottle"]

Choice_keychain=int(input("How many keychains you wanna purchase? If not, enter '0' ,else enter your value: "))
Choice_tshirt=int(input("How many keychains you wanna purchase? If not, enter '0' ,else enter your value: "))
Choice_bottle=int(input("How many keychains you wanna purchase? If not, enter '0' ,else enter your value: "))

if Choice_keychain > 10:
    Choice_keychain["keychain"]=0.65
if Choice_tshirt > 10:
    Choice_tshirt["t-shirt"]=8.00
if Choice_bottle> 10:
    Choice_bottle["bottle"]=8.75

totalkey = Choice_keychain * keychain
totaltshirt = Choice_tshirt * tshirt
totalbottle = Choice_bottle * bottle
grandtotal = totalkey + totaltshirt + totalbottle
    
   
print("Your are purchasing" + str(Choice_keychain)+"keychains" + str(Choice_tshirt)+ "t-shirts, and " + str(Choice_bottle)+ "water bottles.")