height = input()
weight = input()
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi = weight_as_int / (height_as_float * height_as_float )
print(bmi)