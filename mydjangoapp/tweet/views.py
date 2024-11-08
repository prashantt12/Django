from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')

# defining all the functionalities below

# listing all the Tweets
def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetList.html', {'tweets': tweets})

# method to create Tweets
@login_required
def createTweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit= False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm()
    return render(request, 'tweetForm.html', {'form': form})


# method to edit the tweets
@login_required
def editTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweetForm.html', {'form': form})

# method to delete a tweet
def delTweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweetList')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# creating a View such that User can register for the application
def userRegister(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request,user)
            return redirect('tweetList')

    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})