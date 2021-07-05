country_names = input().split(", ")
capitals = input().split(", ")

country_with_capital = {
    country: capital
    for country, capital in zip(country_names, capitals)}

print(*[f"{country} -> {capital}" for country, capital in country_with_capital.items()], sep="\n")