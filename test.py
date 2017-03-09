from validation import Validation

data = {
	'old_password':'@$#%$%$$#$#$#',
	'new_password':'@$#%$%$$#$#$#',
	'new_password_confirmation':'222322222',
	'phone':'0796359038',
	'birthday':'1991/03/04',
	'email':'walid@netlinks.ws',
	'host':'172.30.30.231',
	'website':'www.oogle.com',
	'nationality':'afghan',
	'active':'1',
	"age":"23",
	"email":"walid@netlinks.ws"
}

rules = {
	'old_password':'required|digits|max:20',
	'new_password':'different:old_password|alpha|confirmed',
	'new_password_confirmation':'same:new_password',
	'phone':'phone|required|max:4|min:2|size:23',
	'birthday':'required|date|date_format:%Y/%m/%d',
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