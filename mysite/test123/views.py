from django.shortcuts import render
from .binpacking import solve_knapsack,items
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def shop_listing(request):
    return render(request, 'shop-listing.html')

def genetic(request):
    best_solution = solve_knapsack()
    total_weight = sum(bit * item.weight for bit, item in zip(best_solution.bits, items))

    context = {
        'available_items': [
            {'index': idx + 1, 'value': item.value, 'weight': item.weight}
            for idx, item in enumerate(items)
        ],
        'best_solution_bits': best_solution.bits,
        'best_solution_fitness': best_solution.fitness(),
        'included_items': [
            {'value': item.value, 'weight': item.weight}
            for bit, item in zip(best_solution.bits, items) if bit == 1
        ],
        'total_weight': total_weight,
    }
    return render(request,"binpacking.html", context)