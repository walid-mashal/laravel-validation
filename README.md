### Laravel Validation

**LaravelValidation** is a python class containing logic for implementing Laravel style Data Validation using python language. This code can be used with html forms to validate their input fields and can also be used with any kind of other data as long as the data is in the form of a python dictionary.

For Example we can have some data in the form of a python dictionary as the following:

    data = { 
        'name':'2222222',   
        'phone':'2',  
        'birthday':'1991/03/04',    
        'email':'info@example.com',    
        'host':'172.30.30.231',  
        'website':'https://www.example.com', 
        'nationality':'afghan', 'active':'1',  
    }

that needs to be validated.

So we can write Rules to validate the data in the following way

    rules = { 
        'name':'required|size:20',   
        'phone':'phone', 
        'birthday':'date|date_format:%Y/%m/%d', 
        'email':'required|email', 'host':'ip', 
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

    from laravel_validation import LaravelValidation

    validator = LaravelValidation()
    errors = validator.validate(data,rules)



### Validation Rules

The following is a list of the validation rules available

#### boolean

The field under validation must be able to be cast as a **boolean**. Accepted input values are true, false, 1, 0, "1" and "0".

#### date

The field under validation must be a valid date, the default value for the format is **%m/%d/%Y** if no **date_format** rule is applied.

#### date_format:format

The field under validation must match the format defined in the **format**, the default format is **%m/%d/%Y**. This rule should be preceeded by the **date** rule.

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

#### size:value

The field under validation must have a size matching the given value. For string data, value corresponds to the number of characters. For numeric data, value corresponds to a given integer value.

#### website

The field under validation must have a valid website url as value. for example: https://www.example.com

#### different:field

The given field must be different than the field under validation.

#### same:field

The given field must match the field under validation.
