def register_team(teams, name):

    if not isinstance(name, str):

        raise TypeError("invalid data type")
    
    cleaned_name = name.strip()

    if cleaned_name == "":
        raise ValueError("invalid name")

    if len(cleaned_name) < 2 len(cleaned_name) > 30:
        raise ValueError("Team name must contain 2 to 30 characters")   

        


