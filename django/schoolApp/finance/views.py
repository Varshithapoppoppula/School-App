from django.shortcuts import render

# Create your views here.
def feeCollection(request):
    values={"Name":"Durga prasad","Age":21,"Address":"Tadepalli"}
    return render(request,'finance/fee-Collection.html',values)
def feeCollectionReport(request):
    values={"Name":"Durga prasad","Age":21,"Address":"Tadepalli"}
    return render(request,'finance/fee-CollectionReport.html',values)
def feeDuesReport(request):
    values={"Name":"Durga prasad","Age":21,"Address":"Tadepalli"}
    return render(request,'finance/fee-DuesReport.html',values)
