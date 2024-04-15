from Portfolio.models import Project

project_data = [
    {
        'title': "Portfolio Website",
        'description': "Developed a portfolio about my favorite sports team using Ruby on Rails.",
        'image': "rm-portfolio.png",
        'technologies': ["HTML", "CSS", "JavaScript"],
    },
    {
        'title': "E-commerce App",
        'description': "Built a platform for dog-sitting in the Memphis Area.",
        'image': "woof-sitters.png",
        'technologies': ["Ruby on Rails", "HTML", "CSS"],
    },
]


for data in project_data:
    project = Project(
        title=data['title'],
        description=data['description'],
        image=data['image'],
        technologies=', '.join(data['technologies'])  # Convert list to string
    )
    project.save()