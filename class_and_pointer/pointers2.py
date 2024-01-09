dict1 = {"value": 11}

dict2 = dict1

print("Before value is updated:")
print(f"dict1 = {dict1}")
print(f"dict1 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"dict1 points to: {id(dict2)}")

dict2["value"] = 22

print("\nAfter value is updated:")
print(f"dict1 = {dict1}")
print(f"dict1 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"dict1 points to: {id(dict2)}")
