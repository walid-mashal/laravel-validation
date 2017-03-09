### Validation

**Validation** is a python class containing logic for implementing Laravel style Data Validation using python language. This code can be used with html forms to validate their input fields and can also be used with any kind of other data as long as the data is in the form of a python dictionary.

For Example we can have some data in the form of a python dictionary as the following:

    data = { 
        'name':'2222222',   
        'phone':'2',  
        'birthday':'1991/03/04',    
        'email':'info@example.com',    
        'host':'172.30.30.231',  
        'website':'https://www.example.com', 
        'nationality':'afghan',
        'active':'1',  
    }

that needs to be validated.

So we can write Rules to validate the data in the following way

    rules = { 
        'name':'required|size:20',   
        'phone':'phone', 
        'birthday':'date|date_format:%Y/%m/%d', 
        'email':'required|email',
        'host':'ip', 
        'website':'website', 
        'nationality':'in:afghan,pakistani,irani',
        'active':'boolean'
    }  

Description:

The **name** field is a required field and only allows a maximum value of 20 characters.

The **Phone** field is a telephone number field and a valid phone number should be entered for this field.

The **birthday** field is a date field and the value entered should be a valid date, the date_format allows you to specify a date format that the field should be filled with.

The **email** is also required and a valid email should be entered into that field  

**Host** must be a valid ip address e.g. 196.3.3.8

**Website** must be a valid website address e.g. http://www.google.com  

**Nationality** can be one of the three provided strings: afghan,pakistani,irani  

**Active** must be one of the following: 1,0,"1","0","false","true",False,True


Now we can write the following code to validate the **data**:

    from validation import Validation

    validator = Validation()
    errors = validator.validate(data,rules)

Now the **errors** contain a list of  error messages that is the result of the validation.

We can call the **is_valid()** method to validate the data and will return either **True** or **False** 

    from validation import Validation

    validator = Validation()
    isvalid = validator.is_valid(data,rules)
	
    errors = validator.errors
    
After **validate()** or **is_valid()** there will be an instance variable with the name **errors** set on the object that holds the list of validation error messages.

### Validation Rules

The following is a list of the validation rules available

#### alpha

The field under validation must be entirely alphabetic characters.

#### alpha_num

The field under validation must be entirely alpha-numeric characters.

#### between:min,max

The field under validation must have a size between the given **min** and **max**. Strings and numerics are evaluated in the same fashion as the **size** rule.

#### boolean

The field under validation must be able to be cast as a **boolean**. Accepted input values are true, false, 1, 0, "1" and "0".

#### confirmed

The field under validation must have a matching field of foo_confirmation. For example, if the field under validation is password, a matching password_confirmation field must be present in the input.

#### date

The field under validation must be a valid date, the default value for the format is **%m/%d/%Y** if no **date_format** rule is applied.

#### date_format:format

The field under validation must match the format defined in the **format**, the default format is **%m/%d/%Y**. This rule should be preceeded by the **date** rule.

#### different:field

The given field must be different than the field under validation.

#### digits:value

The field under validation must be numeric and must have an exact length of **value**.

#### email

The field under validation must be formatted as an e-mail address.

#### integer

The field under validation must have an integer value.

#### ip

The field under validation must be formatted as an IP address.

#### max:value

The field under validation must be less than or equal to a maximum value. Strings, numerics, and files are evaluated in the same fashion as the size rule.

#### min:value

The field under validation must have a minimum value. Strings, numerics, and files are evaluated in the same fashion as the size rule.

#### not_in:foo,bar,...

The field under validation must not be included in the given list of values.

#### required

The field under validation must be present in the input data.

#### same:field

The given field must match the field under validation.

#### size:value

The field under validation must have a size matching the given **value**. For string data, value corresponds to the number of characters. For numeric data, **value** corresponds to a given integer value.

#### website

The field under validation must have a valid website url as value. for example: https://www.example.com or www.example.com
