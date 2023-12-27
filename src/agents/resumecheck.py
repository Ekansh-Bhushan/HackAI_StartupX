import requests
from datetime import datetime 
import json
import csv
from uagents import Agent, Context
from src.skill.skillgiver import preprocess_resume
from src.skill.skillgiver import extract_skills


with open('src/jobdescibe.txt', mode = 'r') as jobDescription:
    jobDescribe = jobDescription.readlines()

    

count = shortlistedcount=  0
def readResumeFile(resumepath):
    return extract_skills(preprocess_resume(resumepath))

rank = []

with open('src/resumepath.csv', mode = 'r') as resumepaths:
    resumepaths = csv.reader(resumepaths)
    for resumepath in resumepaths:
        count += 1
        skill = readResumeFile(resumepath)
        if skill:
                matches = list(set(jobDescribe).intersection(skill))
                shortlistedcount += 1
                prob = (matches/ jobDescribe.len())*100
                prob_dict = {resumepath : prob}
                rank.append(prob)

        else:
            continue
                




def ResumeUpdater():
    agent = Agent(name="agent", seed = "agent recover phase")
    @agent.on_interval(period=86400) #update in a day 
    async def ResumeStatusUpdate(ctx: Context):
        ctx.logger.info(f'Today we got these many resume {count} and we have collected the shortisted resume : {shortlistedcount}')
    try:
         if shortlistedcount :
              send_mail_to_user()

    except Exception as e:
         print(e)