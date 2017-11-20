from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
import json

def index(request):

    return render(request, 'app/search.html') 

def show(request):
    user= request.POST.get('username')
    api_url=requests.get('https://api.github.com/users/%s/repos' % user)
    print(api_url.ok)
    if(api_url.ok):
        repoItem = json.loads(api_url.text or api_url.content)
        repo_link=[]
        total_num=0
        repo_name=[]
        username=''
        for i in repoItem:
            full_link=(i['full_name'])
            repo_link.append("https://github.com/"+i['full_name'])
            #spliting username and repository name
            username,name=full_link.split('/')
            repo_name.append(name)
            total_num=total_num+1

        context = {"total_num": total_num, "repo_name": repo_name, "repo_link":repo_link, "username":user}
        return render(request, 'app/result.html', context)
    else:
        context ={"error":"UserName Does not exit"} 
        return render(request, 'app/result.html', context)
    

    
