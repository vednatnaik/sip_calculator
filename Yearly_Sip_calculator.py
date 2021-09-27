import matplotlib
matplotlib.use('WebAgg')
from matplotlib import pyplot as plt

def sip_calculator (sip_amount, years, IntrestRate):

    current_amount = sip_amount
    current_amount = sip_amount + (current_amount * IntrestRate) / 100

    print(f"first month return {current_amount}")

    for n in range(0, years - 1):
        RR = sip_amount + current_amount
        Nextmonthreturn = RR + (RR * IntrestRate) / 100
        # print(RR)
        print(f"your {n + 2} years return is {round(Nextmonthreturn, 2)} Rs/-")
        current_amount = Nextmonthreturn

    print("")
    Invested_amount = sip_amount * years
    total_value = Nextmonthreturn
    est_return = total_value - Invested_amount
    print(f"Invested amount is = {round(Invested_amount, 2)}Rs")
    print("")
    print(f"Estimated return = {round(est_return, 2)}Rs")
    print("")
    print(f"Total Value = {round(total_value, 2)}Rs")
    print("")


    list_data_name = ["Invested Amount", "Est. Returns"]
    list_data = [round(Invested_amount, 2), round(est_return, 2)]
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    fig = plt.figure()
    plt.pie(list_data, labels=list_data_name)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()


print("enter the amout you would like to invest per month:- ")
sip_amount =12*int(input())

print("No. of years:-")
years = int(input())

print("expected rate of return:-")
IntrestRate = int(input())


sip_calculator(sip_amount,years,IntrestRate)