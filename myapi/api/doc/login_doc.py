login_post = {
    # "consumes": [
    #     "application/json"
    # ],
    'securityDefinitions':{
        'JWT':{
            'description': "",
            'type': "apiKey",
            'name': "Authorization",
            'in': "header"
        }

    },
    'parameters': [
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Username'
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Password'
        }
    ],
     "responses": {
        "200": {
          "description": "",

        }
    }
}

