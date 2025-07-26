from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Location, Hotel, FlightTicket, Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def user_logout(request):
    logout(request)
    return redirect('home:home')

def home(request):
    locations = Location.objects.all()
    hotels = Hotel.objects.all()
    categories = ['Vé máy bay', 'Khách sạn', 'Tour', 'Xe đưa đón']
    context = {
        'locations': locations,
        'hotels': hotels,
        'categories': categories,
    }
    return render(request, 'home/home.html', context)

def search(request):
    query = request.GET.get('q', '')
    item_type = request.GET.get('type', 'hotel')  # 'hotel' or 'flight'
    results = []
    if item_type == 'hotel':
        results = Hotel.objects.filter(
            Q(name__icontains=query) | Q(location__name__icontains=query)
        )
    elif item_type == 'flight':
        results = FlightTicket.objects.filter(
            Q(flight_number__icontains=query) | Q(origin__name__icontains=query) | Q(destination__name__icontains=query)
        )
    context = {
        'results': results,
        'query': query,
        'item_type': item_type,
    }
    return render(request, 'home/search.html', context)

def detail(request, item_type, item_id):
    if item_type == 'hotel':
        item = get_object_or_404(Hotel, id=item_id)
    elif item_type == 'flight':
        item = get_object_or_404(FlightTicket, id=item_id)
    elif item_type == 'location':
        item = get_object_or_404(Location, id=item_id)
    else:
        item = None
    context = {
        'item': item,
        'item_type': item_type,
    }
    return render(request, 'home/detail.html', context)

@login_required
def booking(request, item_type, item_id):
    if request.method == 'POST':
        user = request.user
        if item_type == 'hotel':
            hotel = get_object_or_404(Hotel, id=item_id)
            booking = Booking.objects.create(user=user, booking_type='hotel', hotel=hotel, status='confirmed')
        elif item_type == 'flight':
            flight = get_object_or_404(FlightTicket, id=item_id)
            booking = Booking.objects.create(user=user, booking_type='flight', flight=flight, status='confirmed')
        else:
            booking = None
        messages.success(request, 'Đặt chỗ thành công!')
        return redirect('home:orders')
    else:
        if item_type == 'hotel':
            item = get_object_or_404(Hotel, id=item_id)
        elif item_type == 'flight':
            item = get_object_or_404(FlightTicket, id=item_id)
        else:
            item = None
        context = {
            'item': item,
            'item_type': item_type,
        }
        return render(request, 'home/booking.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    return render(request, 'home/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Mật khẩu không khớp.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Tên đăng nhập đã tồn tại.')
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Đăng ký thành công. Vui lòng đăng nhập.')
            return redirect('home:login')
    return render(request, 'home/register.html')

@login_required
def user_orders(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    context = {
        'bookings': bookings,
    }
    return render(request, 'home/orders.html', context)
