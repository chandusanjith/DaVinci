from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'PrivacyPolicy.html')
  
def about_us(request):
    return render(request, 'AboutUs.html')
  
def terms(request):
    return render(request, 'TermsOfUse.html')
