from unittest import TestCase
import sys
sys.path.insert(1,'../laravel_validation')
from validation import Validation

class Test(TestCase):

	def test_validate_regex_data(self):
		field_name = 'month_day' 
		data = { field_name :'5522' } # invalid day of month
		rules = { field_name :r"required|regex:([a-zA-Z]+)" }
		
		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "regex")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_required_data(self):
		field_name = 'old_password'
		data = { field_name :'' } # value is not set for a required field
		rules = { field_name : "required" }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "required")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_same_data(self):
		field_name = 'new_password_confirmation' 
		data = { 
			'new_password' :'@$#%$%$$#$#$#',
			field_name :'222322222' # value of the same field is not same as the identical field
		}
		rules = { field_name :'same:new_password'}

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "same")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_phone_data(self):
		field_name = 'phone' 
		data = { field_name :'06359038' } # not a valid phone number
		rules = { field_name :'phone'}

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "phone")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_date_data(self):
		field_name = 'birthday' 
		data = { field_name:'02-12-2020' } # date does not match the default date format and no date format passed
		rules = { field_name :'date'}

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "date")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_email_data(self):
		field_name = 'email_id' 
		data = { field_name:'zargai' } # not a valid email address
		rules = { field_name :'email' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "email")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_ip_address_data(self):
		field_name = 'host' 
		data = { field_name:'127.5.5' } # invalid ip address
		rules = { field_name :'ip' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "ip")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_website_data(self):
		field_name = 'url' 
		data = { field_name:'www.google' } # invalid website address
		rules = { field_name :'website' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "website")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_in_data(self):
		field_name = 'nationality' 
		data = { field_name:'afghan' } # nationality not one according to the rules
		rules = { field_name :'in:American,Afghan,Arab' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "in")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_boolean_data(self):
		field_name = 'active' 
		data = { field_name:'yes' } # not a valid boolean value
		rules = { field_name :'boolean' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "boolean")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate_between_data(self):
		field_name = 'age' 
		data = { field_name:'12' } # value not between the range in rules
		rules = { field_name :'between:18,64' }

		# creating new instance to have fresh start for validation (have an empty errors global variable of Validation)
		validation = Validation()
		error = validation.validate(data,rules)[0]
		expected_error = validation.return_field_message(field_name, "between")
		self.assertTrue(expected_error == error)

		del validation

	def test_validate(self):
		validation = Validation()
		data = {
			'month_day':'5522',
			'old_password':'asdf',
			'new_password':'@$#%$%$$#$#$#',
			'new_password_confirmation':'222322222',
			'phone':'0796359038',
			'birthday':'02-12-2020',
			'email':'zargai',
			'host':'172.30.30.20',
			'website':'www.oogle.com',
			'nationality':'afghan',
			'active':'1',
			"age":"12",
		}

		rules = {
			'month_day':r"required|regex:([a-zA-Z]+)",
			'birthday':'required|date_format:%m-%d-%Y|after:10-10-1995|before:02-25-2010|date',
			'old_password':'required',
			'new_password':'different:old_password|alpha|confirmed',
			'new_password_confirmation':'same:new_password',
			'phone':'phone|required|max:4|min:2|size:23',
			'email':'required|email|present',
			'host':'ip',
			'website':'website|size:100',
			'nationality':'in:',
			'active':'boolean',
			'age':'between:18,66'
		}

		my_messages = {
			"_comment": "You did not provide any field named <feld_name> in your data dictionary",
			"field_name.rule":"You did not provide any field named field_name in your data dictionary",
			"month_day.regex":"You did not provide any field named month_day in your data dictionary",
			"phone.max":"You did not provide any field named phone in your data dictionary",
			"month_day.required":"You did not provide any field named month_day in your data dictionary",
			"new_password_confirmation.same":"You did not provide any field named new_password_confirmation in your data dictionary",
			"phone.no_field":"You did not provide any field named phone in your data dictionary",
			"birthday.date_format":"You did not provide any field named birthday in your data dictionary",
			"new_password.alpha":"field new_password can only have alphabet values",
			"host.no_field":"You did not provide any field named host in your data dictionary",
			"email.no_field":"You did not provide any field named email in your data dictionary",
			"nationality.no_field":"You did not provide any field named nationality in your data dictionary",
			"active.no_field":"You did not provide any field named active in your data dictionary",
			"age.no_field":"You did not provide any field named age in your data dictionary"
		}

		errors = validation.validate(data,rules) 

		for error in errors:
			print error