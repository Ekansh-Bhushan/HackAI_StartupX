**Automated Resume Screening and Matching Agent** (Team ID: HackAI-230344)

**Introduction:**
In the fast-paced world of recruitment, time is of the essence. Traditional methods of sifting through a mountain of resumes to find the perfect candidate can be time-consuming and inefficient. That's where our innovative resume shortlisting agent comes into play, offering a seamless and intelligent solution for recruiters to expedite the hiring process.

**Key Features:**

**Automated Shortlisting:**
Our cutting-edge machine learning model acts as an autonomous resume analyst, eliminating the need for manual sorting.
The system quickly scans through a plethora of resumes, extracting crucial information to make instant assessments.

**Customizable Criteria:**
Recruiters have the power to define specific criteria for shortlisting, tailoring the model to meet the unique requirements of each job opening.
Parameters such as job title, job description, skills, and years of experience are intelligently evaluated to ensure a perfect match.

**Real-time Application Processing:**
Candidates are evaluated immediately upon submitting their applications, drastically reducing the time between application submission and shortlisting.
Recruiters can act swiftly, ensuring that top talent is identified and engaged promptly.
An agent is added that will include all the shortlisted candidates' details into a csv file.

**Time-Saving Advantage:**
By automating the initial screening process, our model frees up valuable time for recruiters to focus on more strategic aspects of the hiring process.
This time-saving advantage translates into a competitive edge, allowing companies to secure top talent before their competitors.

**Elimination of Bias:**
Our model operates without biases, ensuring that every resume is evaluated objectively based on the defined criteria.
This promotes diversity and inclusivity in the hiring process, as candidates are selected solely on merit.

**Seamless Integration:**
Our solution seamlessly integrates into existing recruitment workflows, providing a hassle-free experience for recruiters.
The system is designed to be user-friendly, requiring minimal training for recruiters to harness its full potential.

**Cost Efficiency:**
The automated nature of our model not only saves time but also reduces operational costs associated with manual resume screening.
Recruiters can allocate resources more efficiently, optimizing the overall cost of the recruitment process.

**INSTRUCTIONS TO RUN THE PROJECT:**
* To create a poetry env.
* Enter sender's email id ,email password in config_email.py
* Enter Mysql password in congif.py file
* Need to create an application password.
* two step verification.
* enable less secure app settings.
* add app password in config_email.py

  
**How our Agent works:**
The recruiter provides the job description and drive link of folder where all the resumes will be stored, to the agent.
 The agent will now use machine learning algorithms to find the keywords from the job description as well as the resumes of the candidates to match the keywords and the candidates are ranked for the job accordingly.
If the resume is shortlisted,the details of that candidate is added in a new CSV file for easy access to the recruiter.

Also, the candidates who will get selected will be notified via email from an agent.
1. Uagents-Runs the code after a specific interval of time and when it reaches above the threshold sends prompt or alert.
2. MYSQL:Uses mysql to stores details of the user i.e. user_email,username,password and the DOB.

![WhatsApp Image 2023-12-27 at 10 17 15 PM](https://github.com/Ekansh-Bhushan/hackaifinal/assets/144479893/0ee86f8a-c5f8-4ccf-a1ae-b34b845aa564)

   
**How are resume rankings done in the agent?**
According to the comparison between the keywords of the resume and the job description, our model generates a probability as to how much is the resume relevant to the job description. According to that probability we are able to rank the resumes for a specific job description.
The probability is calculated by the ratio of keywords matched divided by the total keywords fetched from the job description.
![WhatsApp Image 2023-12-27 at 10 18 38 PM](https://github.com/Ekansh-Bhushan/hackaifinal/assets/144479893/bee6fa64-a20d-4d8f-a978-6beb8df031eb)


**Note:** You can use terminal/command line as well as localhost for trying out the agent.

**Future scope of improvements:**
* We can add more sections to the interface of the recruiter so that he/she can search and segregate candidates on a more complex criteria and can make recruitment process even smaller and concise.
* Further the agent can also be optimized to read more complex and design oriented resumes that are difficult to read.
Focus on human-in-the-loop approaches: Even with AI, the final decision on hiring should involve human judgment and assessment.
Develop candidate-facing tools: Offer a platform for candidates to manage their resumes and applications, creating a more transparent and engaging experience.
Explore ethical AI practices: Implement measures to mitigate bias, promote fairness, and ensure transparency in AI decision-making.

**Beyond Keyword Matching:**
Skills and Experience Parsing: Go beyond keywords to extract and analyze skills and experience mentioned in the resume using Natural Language Processing (NLP) techniques. This will allow for more nuanced matching and identification of transferable skills.
Sentiment Analysis: Analyze the candidate's tone and writing style in the resume to assess cultural fit and communication skills.
Project and Accomplishment Evaluation: Extract and evaluate project details and achievements mentioned in the resume to gauge the candidate's impact and problem-solving abilities.
Education and Certification Verification: Integrate with verification platforms to automatically authenticate educational qualifications and certifications mentioned in the resume.

**Enhanced Candidate Matching:**
Predictive Hiring: Utilize machine learning to predict job performance based on past hiring data and candidate profiles. This can help identify high-potential candidates with a higher chance of success.
Personality and Aptitude Assessments: Integrate with personality and aptitude assessment tools to provide a more holistic view of the candidate's suitability for the role.
Video Interview Scheduling: Automatically schedule video interviews with shortlisted candidates based on their availability and recruiter preferences.

**Expansion and Partnerships:**
Global Reach: Expand your services to cater to international recruitment needs.
Partnerships with Job Boards and Recruitment Agencies: Integrate with job boards and recruitment agencies to reach a wider pool of candidates and employers.
Collaboration with HR Tech Companies: Partner with HR technology companies to offer your agent as a comprehensive recruitment solution.

**Integration with HR Platforms:**
Your system can integrate with popular HR management systems and job portals, offering a seamless experience for recruiters. This integration would streamline the recruitment process, making it more efficient.

**AI-Driven Analytics:**
Implement advanced AI algorithms for more than just keyword matching. Natural Language Processing (NLP) can be used to understand the context and relevance of information in resumes, providing a more nuanced screening.

**Customizable Filtering Criteria:**
Allow recruiters to set customizable filters for various parameters like experience, education, skills, etc., beyond just keyword matching
