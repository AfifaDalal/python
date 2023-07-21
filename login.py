ulist=[]
print('User Login Application:')
print('''Select your Choice: 
	1.Sign for new user
	2.Login for existing user
	3.Delete user
	4.Show all users
	5.Exit''')

ch=0
while(ch!=5):
	ch=int(input('Enter your choice: '))
	if ch==1:
		print('Add User:')
		user={}
		user['username']=input('Enter your Username: ')
		user['password']=input('Enter your Password: ')
		ulist.append(user)
		print('Sign In Successfully')

	if ch==2:
		print('login existing user:')
		for user in ulist:
			username=input('Enter your Username: ')
			password=input('Enter your Password: ')

			if user['username']==username and user['password']==password:
				print('Login Successfully')
				break
			else:
				print('''  Invalid Username or Password.\n   Please try again later''')
				break

	if ch==3:
		print('Delete user:')
		for user in ulist:
			username=input('Enter your Username: ')
			password=input('Enter your password: ')
		if user['username']==username and user['password']==password:
			del user['username']
			del user['password']
			print('User deleted Successfully')
			break
		else:
			print('Invalid user')
			break
	if ch==4:
		print('Showing all users: ')
		for user in ulist:
			print(user)