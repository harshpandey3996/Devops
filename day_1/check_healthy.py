import psutil

thracehold = float(input("Enter cpu thracehold : "))

for i in range (5) :
    cpu = psutil.cpu_percent(interval=1)

    if(cpu >= thracehold) :
        print("Cpu ",{cpu} ," is unhealthy")
    else :
        print("Cpu ",{cpu} ," is healthy")
