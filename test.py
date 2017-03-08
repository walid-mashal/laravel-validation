from validation import Validation

data = {
	'old_password':'@$#%$%$$#$#$#',
	'new_password':'@$#%$%$$#$#$#',
	'repeat_new_password':'222322222',
	'phone':'hame',
	'birthday':'1991/03/04',
	'email':'walid@netlinks.ws',
	'host':'172.30.30.231',
	'website':'google.com',
	'nationality':'afghan',
	'active':'1',
	"age":"23"
}

rules = {
	'old_password':'required|digit|max:20',
	'new_password':'different:old_password|alpha',
	'repeat_new_password':'same:new_password',
	'phone':'phone|required|max:4|min:2|size:23|date',
	'birthday':'required|date|date_format:%Y/%m/%d',
	'email':'required',
	'host':'ip',
	'website':'website|size:3',
	'nationality':'in:afghan,pakistani,irani',
	'active':'boolean',
	'age':'between:18,66'
}

validation = Validation()

is_valid = validation.is_valid(data,rules)

errors = validation.errors

for error in errors:
	print error