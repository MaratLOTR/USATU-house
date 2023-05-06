list_of_lesson_name = ["Oneal",
                            "Duarte",
                            "Brown",
                            "Marsh",
                            "Silva",
                            "Petersen"]
list_of_teacher_name = ["Oneal",
                            "Duarte",
                            "Brown",
                            "Marsh",
                            "Silva",
                            "Petersen",
                            "Mcpherson",
                            "Ferguson",
                            "Hampton",
                            "Nash",
                            "Branch",
                            "Calderon"]
list_of_type_lesson = ['Lecture', 'Practice']
list_of_time_lesson = {1: ['8:00', '9:35'],
                       2: ['9:45', '11:20'],
                       3: ['12:10', '13:45'],
                       4: ['13:55', '15:30']}
group_by_filter = [{
        "faculty": "ФИРТ",
        "data": [
        {
            "course": 1,
            "group": ["МО-111", "ПРО-129"]
        },
        {
            "course": 2,
            "group": ["МО-222", "ПРО-229"]
        },
        {
            "course": 3,
            "group": ["МО-333", "ПРО-329"]
        },
        {
            "course": 4,
            "group": ["МО-444", "ПРО-429"]
        }

        ]
    },
    {
        "faculty": "ИНЭК",
        "data": [
        {
            "course": 1,
            "group": ["И-111", "М-123"]
        },
        {
            "course": 2,
            "group": ["И-222", "М-223"]
        },
        {
            "course": 3,
            "group": ["И-333", "М-323"]
        },
        {
            "course": 4,
            "group": ["И-444", "М-423"]
        }
                ]
    }]

def get_all_group():
    list_of_all_group = []
    for filt in group_by_filter:
            for cour in filt['data']:
                list_of_all_group.extend(cour['group'])
    return list_of_all_group

def get_group_by_filter(faculty: str, course: int):
    for filt in group_by_filter:
        if filt['faculty'] == faculty:
            for cour in filt['data']:
                if cour['course'] == course:
                    return [{'groupName':cour['group']}]