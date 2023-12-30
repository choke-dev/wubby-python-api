import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="wubby_python_api",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="wubby_python_api_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from wubby_python_api.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export wubby_python_api_KEY=value
export wubby_python_api_KEY="@int 42"
export wubby_python_api_KEY="@jinja {{ this.db.uri }}"
export wubby_python_api_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
wubby_python_api_ENV=production wubby_python_api run
```

Read more on https://dynaconf.com
"""
