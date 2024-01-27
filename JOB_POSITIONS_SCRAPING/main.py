from bs4 import BeautifulSoup
import requests
import time

print('Put some skills that you are not familiar with ')
unfamiliar_skill_input= input('>')
unfamiliar_skill= unfamiliar_skill_input.split(',') if unfamiliar_skill_input else []
# unfamiliar_skill= input('>').split(',')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
  html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text
  soup= BeautifulSoup(html_text, 'html.parser')
  jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
  for index, job in enumerate(jobs):
      published_date= job.find('span', class_='sim-posted').span.text
      if 'few' in published_date:
        company= job.find('h3', class_='joblist-comp-name').text
        skills= job.find('span', class_='srp-skills').text.replace(' ','')
        more_info= job.header.h2.a['href']
        # if unfamiliar_skill not in skills: 
        # if not any(skill.strip()in skills for skill in unfamiliar_skill):
        if not unfamiliar_skill or not any(skill.strip() in skills for skill in unfamiliar_skill):
          with open(f'posts/{index}.txt', 'w') as f:
          # company= jobs.find('h3', class_='joblist-comp-name').text.replace(' ','')    to remove spaces
          # print(published_date)

            f.write(f'Company name: {company.strip()} \n')
            f.write(f'Required skills: {skills.strip()} \n')
            f.write(f'More Info:{more_info}')
          print(f'File saved at index: {index}')


if __name__== '__main__':
  while True:
    find_jobs()
    time_wait= 10
    print(f'Waiting {time_wait} minutes...')
    time.sleep(time_wait*60)
