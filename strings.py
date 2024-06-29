chai="  Masala Chai  "
first_char=chai[0]
print(first_char)  #print(chai[0])

# methods
print(chai.lower())

print(chai.upper())

print(chai.strip())          # remove the spaces

print(chai.replace("Masala","Ginger"))

chai1="Lemon, Ginger, Masala, mint"
print(chai1.split())
print(chai1.split(", "))

chai="Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai"))

chai="masala chai chai chai"
print(chai.count("chai"))

chai_type="masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))

for letter in chai:
        print(letter)

chai_variety = ["Lemon", "Masala", "Ginger"]
# print(" ".join(chai_variety))
print(", ".join(chai_variety))

chai = "He said, \"Masala chai is awesome\" "
print(chai)
chai = "Masala\nchai"
print(chai)


#lenth of strings
n=len(chai)
print(n)

# slice
slice_chai = chai[0:6]
print(slice_chai)
# print(chai[0:6])


num_list="0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])              # jump 2
print(num_list[0:7:3])              # jump 3
print(num_list[::-1])               # reverse             

str1 = 'Hello'                      #First string
str2 = 'World!'                     #Second string
str3=str1 + str2                    #Concatenated strings
print(str3)      

st=str1 * 5               # 5 time print "Hello"
print(st)                  