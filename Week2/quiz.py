def greeting(input):
    try:
        name = str(input)
    except:
        name -1
        print("please input your name")
    
    return "Hello" + name

print(greeting("naye"))