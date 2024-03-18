from django.shortcuts import render, redirect
from .forms import InputDataForm
from .models import InputData

def input_data(request):
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            form.save()
            # Process the input data (e.g., run DrugGEN model)
            return redirect('result')  # Redirect to result page after successful submission
    else:
        form = InputDataForm()
    return render(request, 'input_data.html', {'form': form})

def result(request):
    # Logic to retrieve and display results
    # For example, fetching data from the database
    results = InputData.objects.all()  # Fetch all input data from the database

    # Pass the results to the template context
    context = {'results': results}

    return render(request, 'result.html', context)


# from django.shortcuts import render

# # Create your views here.
# # views.py
# from django.http import JsonResponse
# from DrugDisc_Backend.drugdisc_app.gan_models import Generator, SimpleDiscriminator

# def generate_data(request):
#     # Instantiate Generator and SimpleDiscriminator here
#     generator = Generator(...)
#     discriminator = SimpleDiscriminator(...)

#     # Perform actions with the models (e.g., generate data)
#     generated_data = generator(...)
#     discriminator_output = discriminator(...)

#     # Return response
#     return JsonResponse({'generated_data': generated_data, 'discriminator_output': discriminator_output})
