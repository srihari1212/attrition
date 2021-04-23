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
    with popup("Welcome to Attrition predictor"):
        put_text("Kindly fill all the required information to get results")
    Age = input("Enter the age of employee",type = NUMBER,placeholder = "age")
    BusinessTravel = select('Which the type of BusinessTravel?', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    DailyRate = input("Enter the DailyRate of employee",type = NUMBER,placeholder = "range 102 to 1499")
    Department = select('Which the type of Department?', ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = input("Enter the distance from home",type = NUMBER,placeholder = "range 1 to 29")
    Education = select('Which the type of Education?', ['1','2','3','4','5'])
    EducationField = select('Which the field of Education?', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
    EmployeeCount = 1
    EnvironmentSatisfaction = select('Which the Environment Satisfaction level?', ['1','2','3','4'])
    Gender = select('Which the gender of employee?', ['Female', 'Male'])
    HourlyRate  = input("Enter the HourlyRate",type = NUMBER,placeholder = "range 30 to 100")
    JobInvolvement = select('select JobInvolvement level of employee?', ['1','2','3','4'])
    JobLevel = select('select joblevel of employee?', ['1','2','3','4','5'])
    JobRole = select('select the JobRole of employee', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    JobSatisfaction = select('select JobSatisfaction level of employee?', ['1','2','3','4'])
    MaritalStatus =  select('select the marital status of employee?', ['Single', 'Married', 'Divorced'])
    MonthlyIncome  = input("Enter the MonthlyIncome",type = NUMBER,placeholder = "range 1009 to 19999")
    MonthlyRate	  = input("Enter the MonthlyRate",type = NUMBER,placeholder = "range 2094 to 26999")
    NumCompaniesWorked = input("Enter the Number of Companies Worked",type = NUMBER,placeholder = "range 0 to 9")
    OverTime =  select('does the employee do overtime?', ['Yes', 'No'])
    PercentSalaryHike = input("Enter the PercentSalaryHike",type = NUMBER,placeholder = "range 11 to 25")
    PerformanceRating = select('select PerformanceRating', ['1','2','3', '4','5'])
    RelationshipSatisfaction  = select('select Relationship Satisfactionlevel', ['1','2','3', '4'])
    StandardHours = 80
    StockOptionLevel= select('select StockOptionLevel', ['0','1','2','3'])
    TotalWorkingYears = input("Enter the working years",type = NUMBER,placeholder = "range 0 to 40")
    TrainingTimesLastYear = select('select no of TrainingTimesLastYear', ['0','1','2','3','4','5','6'])
    WorkLifeBalance  = select('select WorkLife Balance Satisfactionlevel', ['1','2','3', '4'])
    YearsAtCompany = input("Enter the Years At Company",type = NUMBER,placeholder = "range 0 to 40")
    YearsInCurrentRole	 = input("Enter the Years In CurrentRole",type = NUMBER,placeholder = "range 0 to 18")
    YearsSinceLastPromotion		= input("Enter the Years Since LastPromotion",type = NUMBER,placeholder = "range 0 to 15")
    YearsWithCurrManager	 = input("Enter the Years With CurrManager",type = NUMBER,placeholder = "range 0 to 17")




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
    put_processbar('bar')
    for i in range(1, 11):
        set_processbar('bar', i / 10)
        time.sleep(0.1)
    put_markdown("Here is your result")
    if final == 1:
        put_text('Employee will leave!')
        put_image(open('leave.jpg', 'rb').read())
    else:
        put_text('Employee will stay!')
        put_image(open('stay.jpg', 'rb').read())


app.add_url_rule('/','webio_view',webio_view(attrition),methods = ['GET','POST','OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(attrition, port=args.port)
