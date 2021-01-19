# 密碼重試程式

password = 'a123456'
n = 3

while n > 0:
	user_input = input('請輸入密碼:')
	if user_input == password:
		print('登入成功!')
		break
	else:
		n = n-1
		print('密碼錯誤! 還有', n,'次機會!')
		