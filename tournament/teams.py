def register_team(teams, name):

    if not isinstance(name, str):

        raise TypeError("invalid data type")
    
    cleaned_name = name.strip()

    if cleaned_name == "":
        raise ValueError("invalid name")

    if len(cleaned_name) < 2 or len(cleaned_name) > 30:
        raise ValueError("Team name must contain 2 to 30 characters") 
    
    normalize_name = cleaned_name.casefold()
    for team in teams:
        existing_name = team["name"].casefold()

        if existing_name == normalize_name:
            raise ValueError("Team name alreay exist")    
    
    
    if len(teams) >= 8:
        raise ValueError("Maximum of 8 teams allowed")

    team_number = len(teams) + 1
    team_id = f"TM{team_number:03d}"    
                


