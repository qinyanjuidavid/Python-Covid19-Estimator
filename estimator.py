reportedCases=eval(input('Enter the number of reported cases:-'))
name=input('Enter the name of the region:-')
days=eval(input('Enter the number of days:-'))
totalHospitalbeds=eval(input('Enter the total number of beds available in the reqion:'))
avgDailyIncomeInUsd=eval(input('Enter the Average income:-'))
avgDailyIncomePopulation=eval(input('Enter the average daily income of the population:-'))/100
'''reportedCases=674
name="Africa"
days=28
totalHospitalbeds=1380614
avgDailyIncomeInUsd=1.5
avgDailyIncomePopulation=0.65'''
myinputs={
    "region" : {
        "name": name,
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": avgDailyIncomeInUsd,
        "avgDailyIncomePopulation": avgDailyIncomePopulation
    },
    "periodType": days,
    "timeToElapse": 58,
    "reportedCases": reportedCases,
    "population": 66622705,
    "totalHospitalBeds": totalHospitalbeds }
currentlyInfected=reportedCases*10
currentlyInfectedSevere=reportedCases*50
factor=days/3
factorRounded=round(factor)
InfectionsByRequestedTime=currentlyInfected*(2**factorRounded)
InfectionsByRequestedTimeSevere=currentlyInfectedSevere*(2**factorRounded)
ImpactSevereCasesByRequestedTime=InfectionsByRequestedTime*15/100
SevereCasesByRequestedTime=InfectionsByRequestedTimeSevere*15/100
hospitalBedsByRequestedTime1=totalHospitalbeds*35/95
hospitalBedsByRequestedTimeAtFullCapacity1=totalHospitalbeds*35/100
hospitalBedsByRequestedTime=round(hospitalBedsByRequestedTime1)
hospitalBedsByRequestedTimeAtFullCapacity=round(hospitalBedsByRequestedTimeAtFullCapacity1)
casesForICUByRequestedTime=InfectionsByRequestedTime*5/100
casesForICUByRequestedTimeSevere=InfectionsByRequestedTimeSevere*5/100
casesForVentilatorsByRequestedTime=InfectionsByRequestedTime*2/100
casesForVentilatorsByRequestedTimeSevere=InfectionsByRequestedTimeSevere*2/100
dollarsInFlight=InfectionsByRequestedTime*0.65*1.5*30
dollarsInFlightSevere=InfectionsByRequestedTimeSevere*avgDailyIncomePopulation*avgDailyIncomeInUsd*30
myoutputs={
    'data':{'inputData':myinputs},
    'impact':{
        'currentlyInfected':currentlyInfected,
        'InfectionsByRequestedTime':InfectionsByRequestedTime,
        'SevereCasesByRequestedTime':ImpactSevereCasesByRequestedTime,
        'HospitalBedsByRequestedTime':hospitalBedsByRequestedTime,
        'hospitalBedsByRequestedTimeFullCapacity':hospitalBedsByRequestedTimeAtFullCapacity,
        'casesForICUByRequestedTime':casesForICUByRequestedTime,
        'casesForVentilatorsByRequestedTime':casesForVentilatorsByRequestedTime,
        'dollarsInFlight':dollarsInFlight,
            },
    'severeImpact':{
        "currentlyInfected":currentlyInfectedSevere,
        "InfectionsByRequestedTime":InfectionsByRequestedTimeSevere,
        "SevereCasesByRequestedTime":SevereCasesByRequestedTime,
        'HospitalBedsByRequestedTime':hospitalBedsByRequestedTime,
        'hospitalBedsByRequestedTimeFullCapacity':hospitalBedsByRequestedTimeAtFullCapacity,
        'casesForICUByRequestedTime':casesForICUByRequestedTimeSevere,
        "casesForVentilatorsByRequestedTime":casesForVentilatorsByRequestedTimeSevere,
        'dollarsInFlight':dollarsInFlightSevere

        }
}
print(myoutputs)