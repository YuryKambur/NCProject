SIGNIN_INVALID_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "integer", "const": 1},
        "error": {
            "type": "object",
            "properties": {
                "messages": {
                    "type": "array",
                    "items": {"type": "string"},
                    "contains": {"const": "USER_INVALID_EXCEPTION"}
                },
                "code": {"type": "integer", "const": 1}
            },
            "required": ["messages", "code"]
        },
        "data": {"type": "null"}
    },
    "required": ["status", "error", "data"],
    "additionalProperties": False
}

SIGNIN_SUCCESS_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "integer", "const": 0},
        "error": {"type": "null"},
        "data": {
            "type": "object",
            "properties": {
                "accessToken": {"type": "string", "minLength": 1},  # Изменено с token
                "refreshToken": {"type": "string", "minLength": 1},
                "userId": {"type": "string", "format": "uuid"},  # Это UUID строка, а не integer
                "isRegistered": {"type": "boolean"}
            },
            "required": ["accessToken", "userId"]  # Обязательные поля
        }
    },
    "required": ["status", "error", "data"],
    "additionalProperties": True
}

SIGNIN_MISSING_FIELDS_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "integer", "const": 1},
        "error": {
            "type": "object",
            "properties": {
                "messages": {"type": "array"},
                "code": {"type": "integer"}
            },
            "required": ["messages", "code"]
        },
        "data": {"type": "null"}
    },
    "required": ["status", "error", "data"]
}