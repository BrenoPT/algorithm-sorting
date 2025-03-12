mult1 = 3
mult2 = 5

for i in range(1,1001):
    message = ""
    
    if i % mult1 == 0:
        message += "Fizz!"
    if i % mult2 == 0:
        message += "Buzz!"
        
    if message == "":
        message = i
        
    print(message)
