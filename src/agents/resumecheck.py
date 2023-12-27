import requests
from datetime import datetime 
import json
import csv
from uagents import Agent, Context
from src.skill.skillgiver import preprocess_resume
from src.skill.skillgiver import extract_skills


count = shortlistedcount=  0
def readResumeFile(resumepath):
    return extract_skills(preprocess_resume(resumepath))

with open('src/resumepath.csv', mode = 'r') as resumepaths:
    resumepaths = csv.reader(resumepaths)
    for resumepath in resumepaths:
        skill = readResumeFile(resumepath)



class ResumeChecker:
    def __init__(self):

    


def ResumeUpdater():
    agent = Agent(name="agent", seed = "agent recover phase")
    @agent.on_interval(period=86400) #update in a day 
    async def ResumeStatusUpdate(ctx: Context):
        ctx.logger.info(f'Today we got these many resume {count} and we have collected the shortisted resume : {shortlistedcount}')
     