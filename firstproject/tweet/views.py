from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from django.db.models import Q
import re

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    if not tweets:
        print("No tweets found")
    return render(request, 'tweet_list.html', {'tweets':tweets})

@login_required
def create_form(request):
    if request.method=='POST':
        form= TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request, 'create_form.html', {'form': form})
@login_required
def edit_form(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        form= TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user=request.user
            form.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request, 'create_form.html', {'form': form})    
@login_required
def delete_tweet(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'delete_tweet.html', {'tweet': tweet})

def register(request):
 if request.method=="POST":
     form=UserRegistrationForm(request.POST)
     if form.is_valid():
         user=form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request, user)

         return redirect('tweet_list')
 else:
   form=UserRegistrationForm() 

 return render(request, 'registration/register.html.', {'form': form})

def highlight(text, word):
    if word:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        return pattern.sub(lambda m: f'<mark>{m.group()}</mark>', text)
    return text

def search_tweets(request):
    query = request.GET.get('q', '')
    tweets = []

    if query:
        tweets = Tweet.objects.filter(Q(text__icontains=query))
        # highlight the query in the tweet text
        for tweet in tweets:
            tweet.highlighted_text = highlight(tweet.text, query)

    return render(request, 'tweet_search.html', {'tweets': tweets, 'query': query})