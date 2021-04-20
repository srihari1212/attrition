from pywebio.output import *
from pywebio.input import * 
from flask import Flask, send_from_directory
from  pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH,start_server
import time
from data import encode
from test import ada,gb,xg
import argparse
import statistics
from statistics import mode
app = Flask(__name__)


def attrition():
    Age = input("Enter the age of employee",type = NUMBER)
    BusinessTravel = select('Which the type of BusinessTravel?', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    DailyRate = input("Enter the DailyRate of employee",type = NUMBER)
    Department = select('Which the type of Department?', ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = input("Enter the distance from home",type = NUMBER)
    Education = select('Which the type of Education?', ['1','2','3','4','5'])
    EducationField = select('Which the field of Education?', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
    EmployeeCount = 1
    EnvironmentSatisfaction = select('Which the Environment Satisfaction level?', ['1','2','3','4'])
    Gender = select('Which the gender of employee?', ['Female', 'Male'])
    HourlyRate  = input("Enter the HourlyRate",type = NUMBER)
    JobInvolvement = select('select JobInvolvement level of employee?', ['1','2','3','4'])
    JobLevel = select('select joblevel of employee?', ['1','2','3','4','5'])
    JobRole = select('select the JobRole of employee', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    JobSatisfaction = select('select JobSatisfaction level of employee?', ['1','2','3','4'])
    MaritalStatus =  select('select the marital status of employee?', ['Single', 'Married', 'Divorced'])
    MonthlyIncome  = input("Enter the MonthlyIncome",type = NUMBER)
    MonthlyRate	  = input("Enter the MonthlyRate",type = NUMBER)
    NumCompaniesWorked = input("Enter the Number of Companies Worked",type = NUMBER)
    OverTime =  select('does the employee do overtime?', ['Yes', 'No'])
    PercentSalaryHike = input("Enter the PercentSalaryHike",type = NUMBER)
    PerformanceRating = select('select PerformanceRating', ['1','2','3', '4','5'])
    RelationshipSatisfaction  = select('select Relationship Satisfactionlevel', ['1','2','3', '4'])
    StandardHours = 80
    StockOptionLevel= select('select StockOptionLevel', ['0','1','2','3'])
    TotalWorkingYears = input("Enter the working years",type = NUMBER)
    TrainingTimesLastYear = select('select no of TrainingTimesLastYear', ['0','1','2','3','4','5','6'])
    WorkLifeBalance  = select('select WorkLife Balance Satisfactionlevel', ['1','2','3', '4'])
    YearsAtCompany = input("Enter the Years At Company",type = NUMBER)
    YearsInCurrentRole	 = input("Enter the Years In CurrentRole",type = NUMBER)
    YearsSinceLastPromotion		= input("Enter the Years Since LastPromotion",type = NUMBER)
    YearsWithCurrManager	 = input("Enter the Years With CurrManager",type = NUMBER)




    Gender = int(encode['colname']['Gender'][Gender])
    BusinessTravel = int(encode['colname']['BusinessTravel'][BusinessTravel])
    Department = int(encode['colname']['Department'][Department])
    EducationField = int(encode['colname']['EducationField'][EducationField])
    JobRole = int(encode['colname']['JobRole'][JobRole])
    MaritalStatus = int(encode['colname']['MaritalStatus'][MaritalStatus])
    OverTime = int(encode['colname']['OverTime'][OverTime])
    Education = int(Education)
    EnvironmentSatisfaction = int(EnvironmentSatisfaction)
    JobInvolvement = int(JobInvolvement)
    JobLevel = int(JobLevel)
    JobSatisfaction = int(JobSatisfaction)
    PerformanceRating = int(PerformanceRating)
    RelationshipSatisfaction = int(RelationshipSatisfaction)
    StockOptionLevel = int(StockOptionLevel)
    TrainingTimesLastYear = int(TrainingTimesLastYear)
    WorkLifeBalance = int(WorkLifeBalance)

    data = [Age	,BusinessTravel	,DailyRate,	Department,	DistanceFromHome	,Education,	EducationField,	EmployeeCount	,EnvironmentSatisfaction	,Gender,	HourlyRate,	JobInvolvement	,JobLevel,	JobRole,	JobSatisfaction	,MaritalStatus	,MonthlyIncome	,MonthlyRate,	NumCompaniesWorked	,OverTime	,PercentSalaryHike	,PerformanceRating	,RelationshipSatisfaction,	StandardHours	,StockOptionLevel,	TotalWorkingYears	,TrainingTimesLastYear,	WorkLifeBalance,	YearsAtCompany,	YearsInCurrentRole,	YearsSinceLastPromotion	,YearsWithCurrManager]

    #data = [39,	0,	592	,1,	2	,3,	1	,1,	1	,0,	54,	2	,1,	2	,1,	2,	3646,	17181,	2,	1,	23,	4	,2,	80,	0,	11	,2,	4	,1,	0,	0	,0]
    result=[]
    result.append(ada(data)[0])
    result.append(xg(data)[0])
    result.append(gb(data)[0])
    final = mode(result)
    if final == 1:
        put_text('Employee will leave!')
    else:
        put_text('Employee will stay!')


app.add_url_rule('/','webio_view',webio_view(attrition),methods = ['GET','POST','OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(attrition, port=args.port)