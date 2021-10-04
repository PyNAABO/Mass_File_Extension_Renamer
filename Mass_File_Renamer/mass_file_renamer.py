def rename(FROM,TO,reverse=False):
    if reverse == True:
        FROM,TO = TO,FROM
    else: pass

    import os
    a = os.listdir(os.getcwd())
    for i in a:
        ext = i.split('.')[-1]
        i1 = i.split('.')
        i1 = i1[0]
        if i.split('.')[-1]==FROM:
            os.rename(i,f"{i1}.{TO}")
            print(f"Renamed {i} to {i1}.{TO}")

rename(input("Rename file extension from: "),input("Rename file extension To: "))