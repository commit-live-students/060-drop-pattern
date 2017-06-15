def solution():
    ans=''
    for row in range(0,7):
        for column in range(0,5):
            if(
            ((row==0 or row==6) and (column==0 or column==4))
            or
            ((column==1 or column==2 or column==3) and (row==1 or row==2 or row==4 or row==5))
            or
            (column==1 and row==3)
            or
            (column==4 and row==2)
            ):
                ans=ans+' '
            else:
                ans=ans+'*'
        ans=ans+'\n'
    print ans
solution()
