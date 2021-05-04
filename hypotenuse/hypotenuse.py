from math import sqrt

input_file = open("input.txt", "r")
lines = input_file.readlines()[1:]

values = []
for line in lines:
    values.append(line.split())

for i in values:
    hypo = sqrt(float(i[0])**2 + float(i[1])**2, )
    i.append(f"{hypo:.2f}")

values_in_meter = []
for ii in values:
    l = []
    for jj in ii:
        n = float(jj)*0.3048
        l.append(f"{n:.2f}")
    values_in_meter.append(l)

output_values = sorted(values_in_meter, key=lambda x: float(x[2]))

with open("output.txt", "w") as output_file:
    a = ''
    output_file.writelines(f"legA{a:<5} legB{a:<5} hypotenus{a:<5} \n")
    for j in output_values: 
        output_file.writelines(f"{j[0]:<10} {j[1]:<10} {j[2]:<10} \n")