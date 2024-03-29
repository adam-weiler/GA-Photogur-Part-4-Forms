from django.http import HttpResponse, HttpResponseRedirect #Needed to return an HttpResponse.
from django.urls import reverse
from django.shortcuts import redirect, render #Needed to render the page.
from photogur.models import Picture, CommentForm, Comment #Importing the classes from models.py file.

def pictures_page(request): #Loads all the pictures.
    context = { 'gallery_images': Picture.objects.all(), 'gallery_comments': Comment.objects.all() }

    response = render(request, 'pictures.html', context)
    return HttpResponse(response)




def picture_show(request, id): #Loads an individual picture. #This is the Edit function.
    picture = Picture.objects.get(pk=id)

    form = CommentForm(instance=picture)

    context = {'picture': picture, "form": form}

    response = render(request, 'picture.html', context)
    return HttpResponse(response)




def picture_search(request): #Loads the search results.
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)

    context = {'pictures': search_results, 'query': query}

    #Adding these things
    response = render(request, 'picture_search.html', context)
    return HttpResponse(response)




def create_comment(request): #Saving a comment in the database.
    # # new_comment = Comment() #Instantiates a new_comment.
    picture_id = request.POST['picture'] #Retrieves the picture id from the POST request. (It's hidden.)
    # breakpoint()
    picture = Picture.objects.get(pk=picture_id) #Gets the entire picture object.
    
    # # new_comment.name = request.POST['name'] #Retrieves the name from the POST request.
    # # new_comment.message = request.POST['message'] #Retrieves the message from the POST request.
    # # breakpoint()
    # # new_comment.picture = picture #Sets the foreign key as the picture object.
    
    # # new_comment.save() #Saves the new_comment to the database.
    

    # form = CommentForm(request.POST)
    # # breakpoint()
    # # form.save()

    # context = {'picture': picture}
    # response = render(request, 'picture.html', context)
    # return HttpResponse(response) #Why should this redirect instead of render?

    # # return HttpResponseRedirect(response) #Why should this redirect instead of render?

    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    
    new_comment.picture = picture #Adding this line
    new_comment.save()
    # return HttpResponseRedirect('/')
    context = {'picture':picture}
    # return redirect(reverse('pictures/' + picture_id))

    # return render(request, "picture.html", context) #This is returning to the image page but the form disappears.
    return HttpResponseRedirect(f'/picture/{picture_id}') #Why should this redirect instead of render?