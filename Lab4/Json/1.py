import json
with open("/home/feldy/Coding/PP2/Lab4/Json/sample-data.json", "r") as file:
    data = json.load(file)
print("Interface Status\n======================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")
for item in data['imdata']:
    s1, s2, s3 = item["l1PhysIf"]["attributes"]["dn"], item["l1PhysIf"]["attributes"]["speed"], item["l1PhysIf"]["attributes"]["mtu"]
    if len(s1) == 41: print(f"{s1} {" " * 30} {s2}   {s3}")
    else: print(f"{s1} {" " * (30 - (len(s1) - 41))} {s2}   {s3}")