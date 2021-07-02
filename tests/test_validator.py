from src.validator import Validator


test_data_one = {"email": "test@mail.com", "username": "test"}
test_data_two = {"email": "notemail", "password": "testpassword"}
test_data_three = {"email": "", "password": ""}


class Test_Validation:
    def test_init(self):
        validation = Validator(test_data_one)

        # Assertions
        assert validation.errors_dict == {}
        assert len(validation.errors_dict) == 0
        assert validation.data == test_data_one

    def test__checkValueInErrors(self):
        # test data
        message = "No valid email provided"

        validation_one = Validator(test_data_one)
        validation_two = Validator(test_data_two)
        validation_three = Validator(test_data_three)

        validation_one.check("email")
        validation_two.check("username")
        validation_three.check("email", message=message)

        # Assertions
        assert not validation_one._checkValueInErrors()
        assert validation_two._checkValueInErrors()
        assert validation_three.errors_dict == {"email": message}

    def test_isEmail(self):
        validation_one = Validator(test_data_one)
        validation_two = Validator(test_data_two)

        validation_one.check("email")
        validation_one.isEmail()
        validation_two.check("email")
        validation_two.isEmail()

        # Assertions
        assert validation_one.errors_dict == {}
        assert len(validation_one.errors_dict) == 0
        assert validation_two.errors_dict == {
            "email": "notemail is not a valid email"}
        assert len(validation_two.errors_dict) == 1

    def test_length(self):
        validation_one = Validator(test_data_one)
        validation_one.check("username")
        validation_one.length(minimum=5, maximum=8)

        validation_two = Validator(test_data_two)
        validation_two.check("password")
        validation_two.length(minimum=8, maximum=12)

        # Assertions
        assert validation_one.errors_dict == {
            'username': "username should be between 5 and 8 characters"}
        assert len(validation_one.errors_dict) == 1
        assert validation_two.errors_dict == {}
        assert len(validation_two.errors_dict) == 0

    def test_errors(self):
        validation_one = Validator(test_data_one)
        validation_one.check('email').isEmail()

        validation_two = Validator(test_data_two)
        validation_two.check('email').isEmail()

        # Assertions
        assert len(validation_one.errors_dict) == 0
        assert validation_one.errors_dict == {}
        assert len(validation_two.errors_dict) == 1
        assert validation_two.errors_dict == {
            "email": "notemail is not a valid email"}
