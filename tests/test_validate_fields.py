
from unittest import TestCase
import sys
sys.path.insert(1,'../laravel_validation')
from validation import Validation

class Test(TestCase):

    val_obj = Validation()

    def test_validation_rule_alpha(self):
        errors = self.val_obj.validate_alpha_fields({'name': 'spogmai'}, 'name')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_alpha_fields({'name': 'spogmai12312'}, 'name')
        self.assertFalse(errors == [])

    def test_validation_rule_alpha_num(self):
        errors = self.val_obj.validate_alpha_num_fields({'name': 'spogmai234234324342'}, 'name')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_alpha_num_fields({'name': 'spogmai@#$@##$@234234324342'}, 'name')
        self.assertFalse(errors == [])

    def test_validation_rule_boolean(self):
        errors = self.val_obj.validate_boolean_fields({'is_eligible':0}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':"0"}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':1}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':"1"}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':True}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':'true'}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':'false'}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':False}, 'is_eligible')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':'yes'}, 'is_eligible')
        self.assertFalse(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':'No'}, 'is_eligible')
        self.assertFalse(errors == [])

        errors = self.val_obj.validate_boolean_fields({'is_eligible':'yeah'}, 'is_eligible')
        self.assertFalse(errors == [])

    def test_validation_rule_between(self):
        errors = self.val_obj.validate_between_fields({'age':'44'}, 'age', 'between:18,66')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_between_fields({'age':'100'}, 'age', 'between:18,66')
        self.assertFalse(errors == [])

    def test_validation_rule_confirmed(self):
        errors = self.val_obj.validate_confirmed_fields(
                    {'password':'********', 'password_confirmation': '********'}, 
                    'password', 
                )
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_confirmed_fields(
                    {'password':'********'}, 
                    'password', 
                )
        self.assertFalse(errors == [])

    def test_validation_rule_date(self):
        errors = self.val_obj.validate_date_fields(
	                { 'birthday':'02-12-2020' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date']
                )
        self.assertTrue(errors == [])

        # wrong date format returns errors 
        errors = self.val_obj.validate_date_fields(
	                { 'birthday':'02-12-2020' },
                    'birthday',
                    ['date_format:%mmmm-%d-%Y', 'date']
                )
        self.assertFalse(errors == [])

        # wrong date value does not match date format and returns errors 
        errors = self.val_obj.validate_date_fields(
	                { 'birthday':'022-12-2020' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date']
                )
        self.assertFalse(errors == [])

    def test_validation_rule_before(self):
        errors = self.val_obj.validate_before_date_fields(
	                { 'birthday':'02-12-2000' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date'],
                    'before:02-25-2010'
                )
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_before_date_fields(
	                { 'birthday':'02-12-2020' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date'],
                    'before:02-25-2010'
                )
        self.assertFalse(errors == [])

    def test_validation_rule_after(self):
        errors = self.val_obj.validate_after_date_fields(
	                { 'birthday':'02-12-2020' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date'],
                    'after:02-25-2010'
                )
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_after_date_fields(
	                { 'birthday':'02-12-2000' },
                    'birthday',
                    ['date_format:%m-%d-%Y', 'date'],
                    'after:02-25-2010'
                )
        self.assertFalse(errors == [])

    def test_validation_rule_integer(self):
        errors = self.val_obj.validate_integer_fields({ 'age':'40' },'age')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_integer_fields({ 'age':'forty' }, 'age')
        self.assertFalse(errors == [])

    def test_validation_rule_email(self):
        errors = self.val_obj.validate_email_fields({ 'email':'test@test.test' }, 'email')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_email_fields({ 'email':'email' }, 'email')
        self.assertFalse(errors == [])

    def test_validation_rule_different(self):
        errors = self.val_obj.validate_different_fields(
	                {
                        'new_password':'*****************',
                        'old_password':'******'
                    },
                    'new_password',
                    'different:old_password'
                )
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_different_fields(
	                {
                        'new_password':'*****************',
                        'old_password':'*****************'
                    },
                    'new_password',
                    'different:old_password'
                )
        self.assertFalse(errors == [])


    def test_validation_rule_same(self):
        # validate same values of two fields for same rule
        errors = self.val_obj.validate_same_fields(
	                {
                        'new_password':'*****************',
                        'new_password_confirmation':'*****************'
                    },
                    'new_password',
                    'same:new_password_confirmation'
                )
        self.assertTrue(errors == [])

        # validate different values of two fields for same rule
        errors = self.val_obj.validate_same_fields(
	                {
                        'new_password':'*****************',
                        'new_password_confirmation':'******'
                    },
                    'new_password',
                    'same:new_password_confirmation'
                )
        self.assertFalse(errors == [])

    def test_retrieve_date_format(self):
        df = '%m-%d-%Y'
        df_retrieved = self.val_obj.retrieve_date_format(
	                ['required','date_format:%s' % df, 'after:10-10-1995','before:02-25-2010','date'],
                )
        self.assertTrue(df_retrieved == df)
        df = 'mm-dd-yy'
        df_retrieved = self.val_obj.retrieve_date_format(
	                ['date_format:%s' % df,'date'],
                )
        self.assertTrue(df_retrieved == df)

    def test_match_regular_expression(self):
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        errs, matched = self.val_obj.match_regular_expression(regex, 'w@w.w','email')
        # if the regex matches the value, the matched variable will have an object instead of None
        self.assertTrue(matched != None)
        
        errs, matched = self.val_obj.match_regular_expression(regex, 'ww.w','email')
        self.assertFalse(matched != None)

        regex = r'(http(s)?://)?([\w-]+\.)+[\w-]+[\w-]+[\.]+[\.com]+([./?%&=]*)?'
        errs, matched = self.val_obj.match_regular_expression(regex,'www.test.com','website')
        self.assertTrue(matched != None)

        errs, matched = self.val_obj.match_regular_expression(regex,'www.com','website')
        self.assertFalse(matched != None)

    def test_validate_regex_fields(self):
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        errors = self.val_obj.validate_regex_fields({'email':'www@www.www'}, 'email','regex:%s' % regex)
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_regex_fields({'email':'www www.www'}, 'email','regex:%s' % regex)
        self.assertFalse(errors == [])
        
    def test_validate_max_fields(self):
        errors = self.val_obj.validate_max_fields({'height': '150'}, 'height','max:250')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_max_fields({'height': '251'}, 'height','max:250')
        self.assertFalse(errors == [])

    def test_validate_min_fields(self):
        errors = self.val_obj.validate_min_fields({'height': '150'}, 'height','min:50')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_min_fields({'height': '45'}, 'height','min:50')
        self.assertFalse(errors == [])

    def test_validate_not_in_fields(self):
        errors = self.val_obj.validate_not_in_fields({'height': '150'}, 'height','not_in:50,40,60')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_not_in_fields({'height': '50'}, 'height','not_in:50,40,60')
        self.assertFalse(errors == [])

    def test_validate_in_fields(self):
        errors = self.val_obj.validate_in_fields({'height': '50'}, 'height','in:50,40,60')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_in_fields({'height': '150'}, 'height','in:50,40,60')
        self.assertFalse(errors == [])

    def test_validate_ip_fields(self):
        errors = self.val_obj.validate_ip_fields({'host':'172.30.30.20'}, 'host')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_ip_fields({'host':'172.30.20'}, 'host')
        self.assertFalse(errors == [])

    def test_validate_phone_fields(self):
        errors = self.val_obj.validate_phone_fields({'phone':'0093777777777'}, 'phone')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_phone_fields({'phone':'00937777777'}, 'phone')
        self.assertTrue(errors == [])

    def test_validate_present_fields(self):
        errors = self.val_obj.validate_present_fields({'address':'Some address'}, 'address')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_present_fields({}, 'address')
        self.assertFalse(errors == [])

    def test_validate_size_fields(self):
        errors = self.val_obj.validate_size_fields({'name':'Sabawoon Momand'}, 'name', 'size:23')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_size_fields({'name':'Pasarlay Safi'}, 'name', 'size:10')
        self.assertFalse(errors == [])

    def test_validate_required_fields(self):
        errors = self.val_obj.validate_required_fields({'name':'Zargay Baryalai'}, 'name')
        self.assertTrue(errors == [])

        errors = self.val_obj.validate_required_fields({'name':''}, 'name')
        self.assertFalse(errors == [])

        errors = self.val_obj.validate_required_fields({'age':'25'}, 'name')
        self.assertFalse(errors == [])

    def test_validate_field_rule(self):
        #successful test
        errors = self.val_obj.validate_field_rule({'name':'Zargay Baryalai'}, 'name', 'required')
        self.assertTrue(errors == [])

        # unsuccessful test 
        errors = self.val_obj.validate_field_rule({}, '', 'asdfsdff', '')
        self.assertFalse(errors == [])

    def test_validate_errors_set(self):
        #successful test
        # creating new object to test .errors
        val_obj_new = Validation()
        val_obj_new.validate({'name':'Zargay Baryalai'}, {'name': 'required'})
        self.assertTrue(val_obj_new.errors == [])

        # unsuccessful test 
        val_obj_new.validate({}, {'name':'required'})
        self.assertFalse(val_obj_new.errors == [])
        del val_obj_new

    def test_is_valid(self):
        #successful test
        res = self.val_obj.is_valid({'name':'Zargay Baryalai'}, {'name':'required'})
        self.assertTrue(res)

        #Failing test
        res = self.val_obj.is_valid({'name':'Zargay Baryalai'}, {'name':'digits'})
        self.assertFalse(res)
