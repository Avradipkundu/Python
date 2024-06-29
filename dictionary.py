chai_types={"Masala":"spicy", "Ginger":"zesty", "Green":"Mild"}
print(chai_types)

print(chai_types["Masala"])
print(chai_types.get("Ginger"))

chai_types["Green"]="Fresh"
print(chai_types)

for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai,chai_types[chai])

for key,value in chai_types.items():
    print(key,value)

if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types))

chai_types["Earl Gray"]="citrus"
print(chai_types)

chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()    # remove the item which is last added
print(chai_types)

del chai_types["Green"]
print(chai_types)

chai_types_copy=chai_types.copy()
print(chai_types_copy)

tea_shop={
    "chai":{"Masala":"spicy", "Ginger":"zesty"},
    "tea":{"Green":"Mild", "Black":"strong"}
}
print(tea_shop)
print(tea_shop["tea"])
print(tea_shop["chai"]["Ginger"])

squared_num={x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear()
print(squared_num)

keys=["Masala","Ginger","Lemon"]
default_value="Delicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)

new_dict=dict.fromkeys(keys,keys)
print(new_dict)
