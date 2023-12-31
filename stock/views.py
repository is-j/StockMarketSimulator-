# stock/views.py
import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import Stock
import requests
from datetime import date
import plotly.graph_objs as go
from plotly.offline import plot
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

API_KEY = os.environ.get('API_KEY')

# Stock Detail View: This view provides detailed information about
# a specific stock, including its current price, description,
# and any other relevant data.
class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(reverse('main_page'))


@login_required
def main_page(request):
    # Your main page logic goes here
    return render(request, 'main_profile/main_page.html')


def index(request):
    return HttpResponse("This is the stock index")


def stock_list(request):
    stocks = Stock.objects.all()

    # Retrieve stock data for the graph
    dates = [stock.date for stock in stocks]
    close_prices = [stock.close_price for stock in stocks]
    open_prices = [stock.open_price for stock in stocks]
    high_prices = [stock.high_price for stock in stocks]
    low_prices = [stock.high_price for stock in stocks]

    # Create a line plot using Plotly
    trace = go.Candlestick(
        x=dates,
        open=open_prices,
        high=high_prices,
        low=low_prices,
        close=close_prices,
    )
    data = [trace]
    layout = go.Layout(
        title='Stock Market Data',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price'),
    )
    fig = go.Figure(data=data, layout=layout)

    # Generate the HTML for the graph
    plot_div = plot(fig, output_type='div')

    return render(request, 'stock/stock_list.html', {'stocks': stocks, 'plot_html': plot_div})


def stock_detail(request):
    if request.method == 'POST':
        print(request.POST)
        symbol = request.POST['symbol']  # Symbol of the stock to import
        start_date = request.POST['start_date']  # Start date for data import
        end_date = request.POST['end_date']  # End date for data import
        api_key = 'nOFI_Q8AGlP4FqkozLAP0nukXwxlBkCQ'  # Replace with your Polygon.io API key

        # Make API request to Polygon.io
        url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}?apiKey={api_key}'
        response = requests.get(url)
        data = response.json()

        results = data['results']

        # Process and save data to the database
        for result in results:
            timestamp = result['t']
            date = datetime.datetime.fromtimestamp(timestamp / 1000).date()
            open_price = result['o']
            high_price = result['h']
            low_price = result['l']
            close_price = result['c']
            volume = result['v']

            stock = Stock(
                symbol=symbol,
                date=date,
                end_date=end_date,
                start_date=start_date,
                open_price=open_price,
                high_price=high_price,
                low_price=low_price,
                close_price=close_price,
                volume=volume
            )
            stock.save()

        return HttpResponse("Data imported successfully.")

    return render(request, 'stock/stock_detail.html')
