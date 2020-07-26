from django.shortcuts import render, redirect
from .models import Memo

def home(request) :
    return render(request, 'home.html')

def memo(request) :
    memos = Memo.objects.all()
    return render(request, 'memoField.html', {'memos': memos})

def createMemo(request):
    memo = Memo()
    memo.content = request.GET['text']
    memo.save()
    return redirect('memo')