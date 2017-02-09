from django.conf import settings # import the settings file

def favicon(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    fav=""
    if settings.SERVER=='PROD':
        fav="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAA////AAAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERAAAAASIiIiIQAAASIiIiIiEAASIiIiIiIhASIiIiIiIiIRISISISISIhEiEhISEhIiESISEhISESIRISISEhISEhEhIhISEhISESIRESEiESIRIiIiIiIiIhASIiIiIiIhAAEiIiIiIhAAABIiIiIhAAAAARERERAADwDwAA4AcAAMADAACAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAAwAMAAOAHAADwDwAA"
    elif settings.SERVER=='DEV':
        fav="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAP/3AGNpaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAiIiIiAAAAAhEREREgAAAhERERERIAAhERERERESAhEREREREREiEhEhEhEhESIRISEhISERIhEhISEhIhEiEhEhISEhISISESEhISEhIhEiIhIRIhEiERERERERESAhERERERESAAIRERERESAAACERERESAAAAAiIiIiAADwDwAA4AcAAMADAACAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAAwAMAAOAHAADwDwAA"
    else:
        fav="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAY2loAAD/KgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERAAAAASIiIiIQAAASIiIiIiEAASIiIiIiIhASIiIiIiIiIRISISISISIhEiEhISEhIiESISEhISESIRISISEhISEhEhIhISEhISESIRESEiESIRIiIiIiIiIhASIiIiIiIhAAEiIiIiIhAAABIiIiIhAAAAARERERAADwDwAA4AcAAMADAACAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAAwAMAAOAHAADwDwAA"
    return {'favicon': fav}