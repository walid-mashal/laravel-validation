from validation import Validation

data = {
	'month_day':'',
	'old_password':'2011-02-07',
	'new_password':'@$#%$%$$#$#$#',
	'new_password_confirmation':'222322222',
	'phone':'0796359038',
	'birthday':'10-1090',
	'email':'walid@',
	'host':'172.30.30.231',
	'website':'www.oogle.com',
	'nationality':'afghan',
	'active':'1',
	"age":"23",
}

rules = {
	'month_day':r"required|regex:([a-zA-Z]+)",
	'birthday':'required|date_format:%m-%d-%Y|after:10-10-1995',
	'old_password':'required',
	'new_password':'different:old_password|alpha|confirmed',
	'new_password_confirmation':'same:new_password',
	'phone':'phone|required|max:4|min:2|size:23',
	'email':'required|email|present',
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