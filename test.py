from laravel_validation import LaravelValidation

data = {
	'old_password':'',
	'new_password':'2222222',
	'repeat_new_password':'222322222',
	'phone':'hame',
	'birthday':'1991/03/04',
	'email':'walid@netlinks.ws',
	'host':'172.30.30.231',
	'website':'www.google.com',
	'nationality':'afghan',
	'active':'1',
}

rules = {
	'old_password':'required|digit|max:20',
	'new_password':'different:old_password',
	'repeat_new_password':'same:new_password',
	'phne':'phone|required|max:4|min:2|size:23|date',
	'birthday':'required|date|date_format:%Y/%m/%d',
	'email':'required',
	'host':'ip',
	'website':'website|size:3',
	'nationality':'in:afghan,pakistani,irani',
	'active':'boolean'
}

PyVel = LaravelValidation()
errors = PyVel.validate(data,rules)

for error in errors:
	print error