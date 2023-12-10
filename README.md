# Project Title: MuSE (Museum visualzation with Software Engineering)

## Project Description 
This project aims to address the declining enthusiasm towards museum visits and the threat of climate change on museum preservation by leveraging information visualization concepts. The focus is on creating a software-oriented application, specifically a website, to visually demonstrate the impact of climate change on increasing maintenance costs for museums. The project involves setting up a SQLite database to store and modify relevant data, a frontend to visualize and update the website, and a modal to predict data for information visualization. The goal is to dynamically showcase the need for conservation measures through live visualizations that auto-refresh with the latest data, providing a compelling and interactive platform for raising awareness about the challenges faced by museums in the context of climate change.

## Project Link 
[MuSE](https://muse.pythonanywhere.com/)

## SiteMap

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

## Features:
1. **User Registeration & Authentication System**: Allow users to register for an account and log in to access the website's services.
2. **Data Vizualization**: System provides various interactive features including tooltip.
3. **Safety**: System doesn't expose sensitive data and unauthorized access.
4. **Business Rules**: Multiple Business Rules in place.
5. **Compliance**: Teh website complies with various data protection and privacy laws, including GDPR (General Data Protection Regulation)

## Team Style: 
**Open** (all work on different tasks reviewing and providing feedback to each other)

## Process Model: 
**Waterfall Methodology**
1. Requirements gathering and analysis. 
2. System design 
3. Implementation 
4. Testing 
5. Deployment 
6. Maintenance 

## Locally run the Project
1. Download the Project zip file and unzip it. 
2. Open command prompt from the root directory of the project folder.
3. Run the following commands

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. To reload the data into database for historical load
   
```
python utils/loadData.py
```

5. Open your browser and go to http://127.0.0.1:8000/ to see the result

## Acknowledgements
We would like to acknowledge and express our gratitude to the following individuals for their direction and support:
1. [Professor Cantrell, Gary](mailto:g.cantrell@northeastern.edu)
2. [Professor Bogden, Philip](mailto:p.bogden@northeastern.edu)

## Documentations 

- [Team Member Assignments](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EX5P8NcA8_RPrbeu0clp_fcBFZsz1BVgCHzbNDnqD3FmKw?e=rxfZVM)

- [Project Proposal](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EdftzuZHyuFIs4uX7f4vjYABMj3PcdRgMvPfXcCVV4p70Q?e=KrtPnx)

- [SRS](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EU-awuNUJUNMuIo5YItHi9sBjOPuS__RoHhk-4R2TN9-Ng?e=j4VobD)

- [Team Organization Process Modal](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EcGEk4HMIx1PvHfrKb7obrcBprDcp1bj2TnOkdCa-9zi_A?e=miNkb1)
  
- [Software Design Documentation](https://northeastern-my.sharepoint.com/:w:/r/personal/sait_ar_northeastern_edu/Documents/Group-Project-CS5500/MuSE_SDD.docx?d=wf94f2a608b8d4b658d7dc4eccf2a0672&csf=1&web=1&e=cM5f9r)

- [Team Meeting Notes](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EeFunlkxtaZEnE1xbZNHOUQBhcGJLZGy8NSOaa_ExiUU4g?e=idfeXq)

- [Testing Documentation](https://northeastern-my.sharepoint.com/:w:/g/personal/manne_sa_northeastern_edu/ERR13eX72xhGtSaEFmWtwtkB9c0sBDErUBrplHYhOXlPaw?e=2oYuWi)
  
- [Project Evaluation](https://northeastern-my.sharepoint.com/:w:/g/personal/manne_sa_northeastern_edu/EUM7T8KC2lBLo2CEngHdzlEBLVMlFDdsnJ2-e5vSON0KNw?e=Wd4vr2)

- [Individual Contribution Score](https://northeastern-my.sharepoint.com/:w:/g/personal/sait_ar_northeastern_edu/EewPx0Jlg4NDl3hmBhCJ5nYBkSw0Fv_QHktTUcbaj0kPpA?e=dhh0tu)






