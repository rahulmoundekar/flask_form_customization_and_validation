# Flask WTform Customization and Validation:

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

#### Pre Requisites

  - Web Scraping installation:
     ```
    pip install Flask-WTF
    ```
   
#### What The Form Flask WTF

* Type of Input: These are the field types we imported from wtforms, where StringField is a single-line text field, TextField is a multiline textarea, and so forth. WTForms has a strong collection of input types which includes inputs for things like passwords, date-pickers, multi-select drop-downs, and so forth. We'll get more into these later.
* Label: The first parameter passed to a "field" object is the field's "label," AKA the human-readable name for each field. Labels will carry through to our end users, so we should name our input fields properly.
* Validators: A validator is a restriction put on a field that must be met for the user's input to be considered valid. These are restrictions, such as ensuring a password is a minimum of 8 characters long. An input field can have multiple validators. If the user attempts to submit a form where any field's validators are not fully met, the form will fail and return an error to the user.
* Error Message: Any time a validator is not met, we need to tell the user what went wrong. Thus, every validator has an error message.

#### Note 
    that you don't have to pass request.form to Flask-WTF; it will load automatically. And the convenience validate_on_submit will check if it is a POST request and if it is valid.
