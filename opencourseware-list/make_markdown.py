import json

markdown_file = "README.md"
data = json.loads(open("data.json", "r+").read())

markdown_data = "# OpenCourseWare Courses\n\n"
markdown_data += "![logo](./save_files/mit-ol.png)\n" 
for course in data:
    course_data = "\n---\n\n"
    course_data += f'## {course["Course Title"]}\n\n'
    course_data += f'- **ID**: {course["Course ID"]}\n'
    course_data += f'- **Scope**: {course["Course Scope"]}\n'
    course_data += f'- **Title**: {course["Course Title"]}\n'
    course_data += f'- **Link**: <{course["Course Link"]}>\n'
    if len(course["Professors"]) != 0:
        course_data += '- **Professors**: \n'
        for professor in course["Professors"]:
            course_data += f'\t- {professor}\n'
    if len(course["Topics"]) != 0:
        course_data += '- **Topics**: \n'
        for topic in course["Topics"]:
            course_data += f'\t- {topic}\n'
    course_data += f'- ![{course["Course Title"]}](./save_files/{course["Image Source"]})\n'
    markdown_data += course_data

open(markdown_file, "w+").write(markdown_data)