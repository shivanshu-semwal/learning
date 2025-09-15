from bs4 import BeautifulSoup
import pprint
import re
import json

articles_list = []

def get_detail(article, idx):
    item = {}

    # Extract the course type
    course_type = article.find('div', class_='resource-type').get_text(strip=True).replace('\n', '')
    course_type = re.sub(r'\s+', ' ', course_type)

    # Extract the course title
    course_title = article.find('span', id=f'search-result-{idx-1}-title').get_text(strip=True).replace('\n', '')
    course_title =  re.sub(r'\s+', ' ', course_title)

    # Extract course link
    course_link = article.find('div', class_='lr-row course-title').find('a')['href']

    # Extract the professors
    professors = [prof.get_text(strip=True).replace('\n', '') for prof in article.find_all('a', href=True) if 'Prof.' in prof.get_text()]
    professors = [re.sub(r'\s+', ' ', professor) for professor in professors]

    # Extract the topics
    topics = [topic.get_text(strip=True).replace('\n', '') for topic in article.find_all('a', class_='topic-link')]
    topics = [re.sub(r'\s+', ' ', topic) for topic in topics]

    # Extract the image source link
    image_src = article.find('div', class_='cover-image').find('img')['src']

    course_id = course_type.split('|')[0].strip()
    course_scope = course_type.split('|')[1].strip()
    item["Course ID"] = course_id
    item["Course Scope"] = course_scope
    item["Course Title"] = course_title
    item["Course Link"] = course_link
    item["Professors"] = professors
    item["Topics"] = topics
    item["Image Source"] = image_src.replace('save_files/', '')
    articles_list.append(item)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(open("save.html", "r+").read(), 'html.parser')

# Find all article elements
articles = soup.find_all('article')

# Iterate over each article
for idx, article in enumerate(articles, 1):
    get_detail(article, idx)
    # break

print(json.dumps(articles_list))