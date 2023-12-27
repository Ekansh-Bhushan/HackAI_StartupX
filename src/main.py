
from src.agents.resumecheck import ResumeUpdater
from src.utilis.userDatabase import userDatabase, choice
from backend.server import get_data
import csv

if get_data():
    for data in get_data:
        resume = open('src/resumepath.csv', mode ='a', newline='') 
        writerReume = csv.writer(resume)
    userDatabase()
    choice()
    ResumeUpdater()


else:
    userDatabase()
    choice()
    ResumeUpdater()