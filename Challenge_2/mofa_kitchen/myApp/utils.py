from .models import Recipe


def parse_and_store_recipes(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Assume the format is: title|ingredients|instructions|taste|cuisine_type|prep_time|reviews
            data = line.strip().split('|')
            Recipe.objects.create(
                title=data[0],
                ingredients=data[1],
                instructions=data[2],
                taste=data[3],
                cuisine_type=data[4],
                preparation_time=int(data[5]),
                reviews=float(data[6]),
            )
