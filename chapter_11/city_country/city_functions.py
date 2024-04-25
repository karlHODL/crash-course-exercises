def get_formatted_location(city, country, population=''):
    """Generate a neatly formatted location."""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()