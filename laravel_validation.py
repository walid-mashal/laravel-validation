import re, datetime, sys

class LaravelValidation():
	def validate(self, data, rules):
		"""Validate the 'data' according to the 'rules' given, returns a list of errors name 'errors'"""

		errors=[]
	
		#iterate through the rules dictionary, fetching each rule name (dictionary key) one by one
		for field_name in rules:

			#fetch the rule (value of dictionary element) from "rules" dictionary for the current rule name (dictionary key) and split it to get a list
			field_rules = rules[field_name].split('|')
			
			#field_errors will keep the errors for a particular field, which will be appended to the main "errors" list
			field_errors = []

			#now looping through rules of one field one rule at a time with each iteration
			for rule in field_rules:

				#if the field has a "required" rule assigned
				if rule == "required":
					field_errors.extend(self.__validate_required_fields(data, field_name))

				#if the field has a "phone" rule assigned
				elif rule == "phone":
					field_errors.extend(self.__validate_phone_fields(data, field_name))

				#if the field has a "date" rule assigned
				elif rule == "date":
					field_errors.extend(self.__validate_date_fields(data,field_name,field_rules))

				#if the field has a "max" rule assigned
				elif rule.startswith("max"):
					field_errors.extend(self.__validate_max_fields(data,field_name,rule))

				#if the field has a "min" rule assigned
				elif rule.startswith("min"):
					field_errors.extend(self.__validate_min_fields(data,field_name,rule))

				elif rule.startswith("size"):
					field_errors.extend(self.__validate_size_fields(data,field_name,rule))

				#if the field has a "digit" rule assigned
				elif rule == "digit":
					field_errors.extend(self.__validate_integer_fields(data,field_name))

				#if the field has a "boolean" rule assigned
				elif rule == "boolean":
					field_errors.extend(self.__validate_boolean_fields(data,field_name))

				#if the field has a "ip" rule assigned
				elif rule == "ip":
					field_errors.extend(self.__validate_ip_fields(data,field_name))

				#if the field has a "website" rule assigned
				elif rule == "website":
					field_errors.extend(self.__validate_website_fields(data,field_name))

				#if the field has a "not_in" rule assigned
				elif rule.startswith("not_in"):
					field_errors.extend(self.__validate_not_in_fields(data,field_name,rule))

				#if the field has a "in" rule assigned
				elif rule.startswith("in"):
					field_errors.extend(self.__validate_in_fields(data,field_name, rule))

				#if the field has a "different" rule assigned
				elif rule.startswith("different"):
					field_errors.extend(self.__validate_different_fields(data,field_name, rule))

				#if the field has a "same" rule assigned
				elif rule.startswith("same"):
					field_errors.extend(self.__validate_same_fields(data, field_name, rule))

			#combine the errors of current field with the global errors list
			errors.extend(field_errors);

		return errors

	def __validate_required_fields(self, data, field_name):
		"""Used for validating required fields, returns a list of error messages"""

		errs = []
		try:
			if data[field_name] == '':
				 errs.append(field_name + " must be filled")
		except KeyError:
			errs.append("No Field named " + field_name + " to validate for required value")
			return []

		return errs        

	def __validate_date_fields(self, data, field_name, field_rules):
		"""Used for validating date fields, returns a list of error messages"""

		errs = []

		#loop through each rule for the particular field to check if there is any date_format rule assigned
		for rule in field_rules:

			#if there is a date_format rule assigned then fetch the date format from that
		 	if rule.startswith("date_format"):

				df_format_index = field_rules.index(rule)

				date_format = field_rules[df_format_index].split(":")[1]

			#or if there is no date_format assigned then use a default format for validation
			else:
				date_format = '%m/%d/%Y'
		try:
			 datetime.datetime.strptime(data[field_name], date_format)
		except ValueError:
			 errs.append(field_name + " must be a valid date")
		except KeyError:
			 errs.append("No Field named %s to validate for Date value" % (field_name))
			
		return errs

	def __validate_integer_fields(self, data, field_name):
		"""Used for validating integer fields, returns a list of error messages"""

		errs = []
		try:
			if not data[field_name].isdigit():
				errs.append(field_name + " must be an integer")
		except KeyError:
			errs.append("No Field named %s to validate for integer value" % (field_name))
		return errs


	def __validate_email_fields(self, data, field_name):
		"""Used for validating email fields, returns a list of error messages"""

		comp_re = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

		errs = []
		try:	
			result = comp_re.match(data[field_name])
		except KeyError:
			result = "error"
			errs.append("No Field named %s to validate for Phone Number value" % (field_name))
		if not result:
			errs.append(field_name + " must be a valid email")
		return errs

	def __validate_boolean_fields(self, data, field_name):
		"""Used for validating boolean fields, returns a list of error messages"""

		errs = []

		bool_values = [1,0,"1","0","false","true",False,True]
		try:
			if data[field_name] not in bool_values:
				errs.append(field_name + " must be a valid one of the following " + str(bool_values))
		except KeyError:
			errs.append("No Field named %s to validate for boolean value" % (field_name))
		return errs

	def __validate_ip_fields(self, data, field_name):
		"""Used for validating fields having IP Address, returns a list of error messages"""

		comp_re = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

		errs = []
		try:
			result = comp_re.match(data[field_name])
		except KeyError:
			result = "error"
			errs.append("No Field named %s to validate for IP Address value" % (field_name))

		if not result:
			errs.append(field_name + " must be a valid IP Address")
		return errs

	def __validate_phone_fields(self, data, field_name):
		 """Used for validating fields having phone numbers, returns a list of error messages"""

		 comp_re = re.compile(r'^(?:\+?93)?[07]\d{9,13}$')

		 errs = []
		 try:
			 result = comp_re.match(data[field_name])
		 except KeyError:
			 errs.append("No Field named "+field_name+" to validate as a phone number")
			 result = "error"

		 if not result:
			 errs.append(field_name + " must be a valid phone number")
		 return errs

	def __validate_website_fields(self, data, field_name):
		 """Used for validating fields having website addresses, returns a list of error messages"""

		 comp_re = re.compile(r'^(?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/?|[/?]\S+)$', re.IGNORECASE)

		 errs = []
		 try:
		 	 result = comp_re.match(data[field_name])
		 except KeyError:
			 result = "error"
			 errs.append("No Field named %s to validate for a website url value" % (field_name))

		 if not result:
			 errs.append(field_name + " must be a valid Website URL")
		 return errs

	def __validate_max_fields(self, data, field_name, rule):
		 """Used for validating fields for a maximum integer value, returns a list of error messages"""

		 #retrieve the value for that max rule
		 max_value = int(rule.split(':')[1])

		 errs = []
		 try:
			 if data[field_name].isdigit():
				 if int(data[field_name]) > max_value:
					 errs.append("The maximum value of the " + field_name+ " can be " + str(max_value))
			 else:
				 if len(data[field_name]) > max_value:
					 errs.append("The maximum number of characters in the value of the " + field_name + " can be " + str(max_value)+" characters")
		 except KeyError:
			 errs.append("No Field named %s to validate for maximum value" %(field_name))

		 return errs

	def __validate_min_fields(self, data, field_name, rule):
		 """Used for validating fields for a minimum integer value, returns a list of error messages"""

		 #retrieve the value for that min rule
		 min_value = int(rule.split(':')[1])

		 errs = []
		 try:
			if data[field_name].isdigit():
				if int(data[field_name]) < min_value:
					errs.append("The minimum value of the " + field_name + " can be " + str(min_value))
			else:
				if len(data[field_name]) < min_value:
					errs.append("The number of characters in the value of the " + field_name + " must be atleast " + str(min_value)+" characters")
		 except KeyError:
			errs.append("No Field named %s to validate for minimum value" % (field_name))

		 return errs

	def __validate_size_fields(self, data, field_name, rule):
		 """Used for validating fields for a maximum number of characters in a string value, returns a list of error messages"""

		 #retrieve the value for that size rule
		 size_value = int(rule.split(':')[1])

		 errs = []
		 try:
			 if len(data[field_name]) >= size_value:
				 errs.append("The number of characters in " + field_name + " must be " + str(size_value))
		 except KeyError:
			 errs.append("No Field named %s to validate for a size rule" % (field_name))

		 return errs

	def __validate_not_in_fields(self, data, field_name, rule):
		 """Used for validating fields for some number of values to avoid, returns a list of error messages"""

		 #retrieve the value for that not_in rule
		 ls = rule.split(':')[1].split(',')

		 errs = []
		 try:
			 if data[field_name] in ls:
				 errs.append(field_name + " must not be one of these: " + str(ls))
		 except KeyError:
			 errs.append("No Field named %s to validate for not_in rule" % (field_name))

		 return errs

	def __validate_in_fields(self, data, field_name, rule):
		 """Used for validating fields for some number of values to allow, returns a list of error messages"""

		 #retrieve the value for that in rule
		 ls = rule.split(':')[1].split(',')

		 errs = []
		 try:
			 if data[field_name] not in ls:
				 errs.append(field_name + " must not be one of these: " + str(ls))
		 except KeyError:
			 errs.append("No Field named %s to validate for IN Rule" % (field_name))
		 return errs


	def __validate_different_fields(self, data, field_name, rule):
		 """Used for validating fields for some number of values to allow, returns a list of error messages"""

		 #retrieve the value for the different rule
		 ls = rule.split(':')[1].split(',')
		 errs = []
		 try:
			 if data[field_name] == data[ls[0]]:
				 errs.append(field_name+ " must not be the same as " + str(ls[0]))
		 except KeyError:
			 errs.append("No Field named %s to validate for the DIFFERENT Rule" % (field_name))
		 except Exception:
			 errs.append("Error Occured",sys.exc_info())
 		 
		 return errs

	def __validate_same_fields(self, data, field_name, rule):
		 """Used for validating fields for some number of values to allow, returns a list of error messages"""

		 #retrieve the value for the different rule
		 ls = rule.split(':')[1].split(',')
		 errs = []

		 try:
			 if data[field_name] != data[ls[0]]:
				 errs.append(field_name+ " must be the same as " + str(ls[0]))
		 except KeyError:
			 errs.append("No Field named %s to validate for the SAME Rule" % (field_name))
		 return errs