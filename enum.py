#! python3
    s ="hello"
    print(enumerate(s))
    e = enumerate(s)

    for i in e:
        print(i)
    print(e)
	
	
'''
<enumerate object at 0x000001816B3D7E10>
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
<enumerate object at 0x000001816B3D7E10>
'''