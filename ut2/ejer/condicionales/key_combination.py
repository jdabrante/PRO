key1 = input('Key 1:')
key2 = input('Key 2:')
key3 = input('Key 3:')
action = ''
if key1 == 'Ctrl' and key2 == 'Alt' and key3 == 'Del':
    action = 'Log out' 
elif key1 == 'Ctrl' and key2 == 'C':
    action = 'Copy'
elif key1 == 'Ctrl' and key2 == 'V':
    action = 'Paste'
    
print(action)
