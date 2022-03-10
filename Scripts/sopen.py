file = open("test.txt", "r")

try:
    file.write("Hello \n")
except Exception as e:
    print(f"error with (e)")
finally:
    file.close()


