user_resource_get = {
    'parameters': [{
        'name': 'user_id',
        'in': 'path',
        'type': 'integer',
        'required': False,
        'description': 'id'
    }],
     "responses": {
        "200": {
          "description": "A list of users",
          "schema": {
            'id': 'User',
              'properties':{
                'id':{
                  'type': 'integer',
                  'description': 'User ID',
                  'default': ''
                },
                'username':{
                  'type': 'string',
                  'description': 'User username',
                  'default': ''
                },
                'email':{
                  'type': 'string',
                  'description': 'User email',
                  'default': ''
                },
                'password':{
                  'type': 'number',
                  'description': 'User password',
                  'default': ''
                },
                'active':{
                  'type': 'integer',
                  'description': 'User status',
                  'default': ''
                }
              }
          }
        }
    }
}

post = {
    'parameters': [
        {
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Gas station name'
        },
        {
            'name': 'place_id',
            'in': 'formData',
            'type': 'integer',
            'required': False,
            'description': 'Gas station place_id'
        },
        {
            'name': 'latitude',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': True,
            'description': 'Gas station latitude'
        },
        {
            'name': 'longitude',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': True,
            'description': 'Gas station longitude'
        },
        {
            'name': 'rating',
            'in': 'formData',
            'type': 'number',
            'format': 'float',
            'required': False,
            'description': 'Gas station longitude'
        },
        {
            'name': 'vicinity',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Gas station vicinity'
        },
    ],
     "responses": {
        "200": {
          "description": "A gas station created.",

        }
    }
}

