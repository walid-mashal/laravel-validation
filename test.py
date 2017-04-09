from validation import Validation

data = {
	'old_password':'2011-02-07',
	'new_password':'@$#%$%$$#$#$#',
	'new_password_confirmation':'222322222',
	'phone':'0796359038',
	'birthday':'10-10-1999',
	'email':'walid@netlinks.ws',
	'host':'172.30.30.231',
	'website':'www.oogle.com',
	'nationality':'afghan',
	'active':'1',
	"age":"23",
	"email":"walid@netlinks.ws"
}

rules = {
	'birthday':'required|date_format:%m-%d-%Y|before:10-10-1995',
	'old_password':'required',
	'new_password':'different:old_password|alpha|confirmed',
	'new_password_confirmation':'same:new_password',
	'phone':'phone|required|max:4|min:2|size:23',
	'email':'required|email',
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