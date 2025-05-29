from django.shortcuts import render
import random
from .models import flags

def guess_flag(request):
    flagg = list(flags.objects.all())
    if not flagg:
        return render(request, "no_flag.html")

    message = ''

    shown_flags = request.session.get('shown_flags', [])

    if request.method == 'POST':
        guess = request.POST.get('guess', '').strip().lower()
        flag_id = request.session.get('flag_id')
        try:
            flag = flags.objects.get(id=flag_id)
        except flags.DoesNotExist:
            flag = random.choice(flagg)
            message = "Something went wrong. Try again."
        else:
            if guess == flag.country_name.lower():
                message = '✅ Correct!'
            else:
                message = f'❌ Wrong! It was {flag.country_name}.'
            
            if flag.id not in shown_flags:
                shown_flags.append(flag.id)

    remaining_flags = [f for f in flagg if f.id not in shown_flags]

    if not remaining_flags:
        shown_flags = []
        remaining_flags = flagg
        message += " 🔁 New round started!"

    next_flag = random.choice(remaining_flags)

    request.session['flag_id'] = next_flag.id
    request.session['shown_flags'] = shown_flags

    return render(request, 'guess_flag.html', {
        'flag': next_flag,
        'message': message
    })


