from django.shortcuts import render
from joblib import load

#First we put the saved model into a variable called model
model = load('./savedModels/insuranceModel.sav')

#This is a function to get and display the main.html page where you will input the values
def predictor(request):
    return render(request, 'main.html')

#this is the funtion for the form inputs
def formInfo(request):
    months_as_customer = request.GET['months_as_customer']
    age = request.GET['age']
    policy_csl = request.GET['policy_csl']
    policy_deductable = request.GET['policy_deductable']
    policy_annual_premium = request.GET['policy_annual_premium']
    umbrella_limit = request.GET['umbrella_limit']
    insured_sex = request.GET['insured_sex']
    insured_education_level = request.GET['insured_education_level']
    insured_occupation = request.GET['insured_occupation']
    insured_relationship = request.GET['insured_relationship']
    capital_gains = request.GET['capital_gains']
    capital_loss = request.GET['capital_loss']
    incident_type = request.GET['incident_type']
    collision_type = request.GET['collision_type']
    incident_severity = request.GET['incident_severity']
    authorities_contacted = request.GET['authorities_contacted']
    incident_hour_of_the_day = request.GET['incident_hour_of_the_day']
    number_of_vehicles_involved = request.GET['number_of_vehicles_involved']
    property_damage = request.GET['property_damage']
    bodily_injuries = request.GET['bodily_injuries']
    witnesses = request.GET['witnesses']
    police_report_available = request.GET['police_report_available']
    total_claim_amount = request.GET['total_claim_amount']
    injury_claim = request.GET['injury_claim']
    property_claim = request.GET['property_claim']
    vehicle_claim = request.GET['vehicle_claim']
    


#This logic is a  bit faulty, y_pred is suppose to return an accuracy and if that is less than a threshold of 0.5 then the case is a fraud case 
    y_pred = model.predict([[months_as_customer, age, policy_csl, policy_deductable, policy_annual_premium, umbrella_limit, insured_sex, 
                             insured_education_level, insured_occupation, insured_relationship,capital_gains
                             ,capital_loss,incident_type,collision_type,incident_severity,authorities_contacted,incident_hour_of_the_day,number_of_vehicles_involved,property_damage,bodily_injuries,
                             witnesses,police_report_available,total_claim_amount,injury_claim,property_claim,vehicle_claim]])
    if y_pred[0] == 0:
        y_pred = 'This is a Legit Case'
    else:
        y_pred = 'This is a Fraud Case'

    return render(request,'result.html', {'result':y_pred})
