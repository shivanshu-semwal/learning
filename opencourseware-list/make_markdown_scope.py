import json


def generate_data(data):
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
    return markdown_data

graduate_markdown_file = "README_graduate.md"
undergrad_markdown_file = "README_undergrad.md"

data = json.loads(open("data.json", "r+").read())
data_grad = [item for item in data if ("Graduate" in item["Course Scope"])]
data_undergrad = [item for item in data if ("Undergraduate" in item["Course Scope"])]

open(undergrad_markdown_file, "w+").write(generate_data(data_undergrad))
open(graduate_markdown_file, "w+").write(generate_data(data_grad))