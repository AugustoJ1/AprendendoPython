def main():
    #Primeira forma
    i=0
    while i < 21:
        i += 1
        if i==15:
            break
        if i%2 != 0:
            continue
        print(i)
    #Segunda forma
    for i in range(20):
        if i%2==0 and i<15:
            print(i)

main()