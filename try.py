try:
    num = 2 + 'str'
    print('number error')
except:
    print('cant add')
else:
	print('No errors')
finally:
    print('always executed')
    
print('continue')    


,,,
2+ 2

number error
No errors
always executed
continue


2+ 'str'

cant add
always executed
continue

'''