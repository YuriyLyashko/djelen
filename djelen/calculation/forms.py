from django import forms

class Texts:
    сentral_title = "Розрахунок вартості спожитої електроенергії для однозонного лічильника."

    pointer_date_saving_tariffs = "Дата збереження тарифів:"

    header_of_block_tariffs = "Діючі тарифи на електроенергію, грн. за 1 кВт∙год."
    pointer_tariff_limit_to = "за обсяг, спожитий до"
    pointer_kwh_month = "кВт∙год електроенергії на місяць "
    pointer_including = '(включно):'
    pointer_tariff_limit_over = "за обсяг, спожитий понад"
    pointer_kwh = 'кВт∙год до'


    header_of_block_consumption = "Спожита електроенергія."
    date_meter_tariffs = "Введіть дату зняття показів:"
    previous_shows = "Введіть попередні значення лічильника електроенергії:"
    current_shows = "Введіть поточні значення лічильника електроенергії:"
    text_or = "АБО"
    amount_of_electricity = "Введіть кількість спожитої електроенергії, кВт∙год:"

    header_of_block_cost_calculation = "Розрахунок вартості."
    pointer_amount_of_electricity_in_tariff_1 = "обсяг, спожитий до               кВт∙год електроенергії "
    mark_x = "x                  ="
    pointer_amount_of_electricity_in_tariff_2 = "обсяг, спожитий понад               кВт∙год " \
                                                "до               кВт∙год електроенергії на місяць (включно):"
    pointer_amount_of_electricity_in_tariff_3 = "обсяг, спожитий понад               кВт∙год електроенергії на місяць:"
    pointer_total_amount_of_money = "Всього:"
