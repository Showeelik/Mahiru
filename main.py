from external_api import output_data
from processing import output_price_day_week_data_json



if __name__ == '__main__':
    city = input("Введите город: ")
    output_data(city)
    print("")
    output_price_day_week_data_json()
