
from unittest import TestCase
import sys
sys.path.insert(1,'../laravel_validation')
from validation import Validation

class Test(TestCase):

    val_obj = Validation()

    def test_loading_error_message_templates(self):
        va_json_data = self.val_obj.get_error_message_templates()
        
        self.assertTrue(type(va_json_data) == dict)
        
        data_keys = va_json_data.keys()
        
        valid_keys_list = [
            'after', 'alpha', 'alpha_num', 'before', 'between', 'boolean', 'confirmed', 'date', 
            'digits', 'different', 'email', 'in', 'ip', 'max', 'min', 'not_in', 'present', 'phone', 
            'regex', 'required', 'same', 'size', 'website', 'no_field'
        ]

        for key in valid_keys_list:
            self.assertTrue(key in data_keys)

    def test_loading_custom_error_messages(self):
        va_json_data = self.val_obj.get_custom_error_messages()
        
        self.assertTrue(type(va_json_data) == dict)
        
        data_keys = va_json_data.keys()
        
        valid_keys_list = [
        	"_comment", "field_name.rule", "month_day.regex", "phone.max", "month_day.required",
	        "new_password_confirmation.same", "phone.no_field", "birthday.date_format", "new_password.alpha",
        	"host.no_field", "email.no_field", "nationality.no_field", "active.no_field", "age.no_field"
        ]

        for key in valid_keys_list:
            self.assertTrue(key in data_keys)
