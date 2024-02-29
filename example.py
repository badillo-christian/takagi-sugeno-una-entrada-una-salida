from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np

from lkfuzzy import *


def main():
    food = InputVariable('food', range=[0, 10])
    
    food['baja'] = TriangularFunction(0, 0, 5)
    food['regular'] = TriangularFunction(0, 5, 10)
    food['excelente'] = TriangularFunction(5, 10, 10)

    #service['baja'] = TriangularFunction(0, 0, 5)
    #service['regular'] = TriangularFunction(0, 5, 10)
    #service['excelente'] = TriangularFunction(5, 10, 10)

    rules = [
        #Rule(food['baja'] & service['baja'], 0),
        #Rule(food['excelente'] & service['excelente'], 20),
        #Rule(food['regular'], 10),
        #Rule(food['baja'] & service['excelente'], 10),
        #Rule(food['excelente'] & service['baja'], 5),

        Rule(food['baja'], 0),
        Rule(food['regular'], 10),
        Rule(food['excelente'] , 20),

    ]

    system = FuzzySystem(rules)

    test_on_examples(system)
    #draw_heatmap(system)


def test_on_examples(system):
#    ValorPrueba = namedtuple('valorPrueba', 'food service')

#    valoresPrueba = [
#        ValorPrueba(10, 10),
#        ValorPrueba(4, 4),
#        ValorPrueba(0, 0),
#        ValorPrueba(10, 0),
#        ValorPrueba(0, 10),
#        ValorPrueba(2, 6),
#        ValorPrueba(6, 2),
#    ]

    ValorPrueba = namedtuple('valorPrueba', 'food')

    valoresPrueba = [
        ValorPrueba(10),
        ValorPrueba(4),
        ValorPrueba(1),
        ValorPrueba(0),
        ValorPrueba(0.5),
        ValorPrueba(3),
        ValorPrueba(5),
        ValorPrueba(2),
        ValorPrueba(6),
        ValorPrueba(7),
        ValorPrueba(7.5),
        ValorPrueba(9.5),
        ValorPrueba(0.5),
        ValorPrueba(7.3),

    ]

    x = []
    y = []
    i = 0
    for valorPrueba in valoresPrueba:
        
        #tip = system.compute(food=valorPrueba.food, service=valorPrueba.service)
        #print(f'food: {valorPrueba.food:2}/10, service: {valorPrueba.service:2}/10 -> tip: {tip:.1f}%')

        propina = system.compute(food=valorPrueba.food)
        print(f'valor entrada calificación comida: {valorPrueba.food:2}/10 -> propina calculada usando TSK: {propina:.1f}%')
        x.append(valorPrueba.food)
        y.append(propina)
    plt.plot(x,y)

    plt.xlabel(' Calidad Comida')
    plt.ylabel(' % Propina')
    plt.title('Calidad Comida vs % Propina')
    plt.show()    

def draw_heatmap(system):
    resolution = 20
    food_values = np.linspace(0, 10, resolution)
    service_values = np.linspace(0, 10, resolution)

    food_grid, service_grid = np.meshgrid(food_values, service_values)
    tip_grid = np.zeros_like(food_grid)
    for food_index in range(resolution):
        for service_index in range(resolution):
            food_value = food_values[food_index]
            service_value = service_values[service_index]
            tip_grid[food_index, service_index] = system.compute(food=food_value, service=service_value)

    fig, ax = plt.subplots()
    cp = ax.contourf(service_grid, food_grid, tip_grid, 200)

    ax.set_xlabel('Service quality')
    ax.set_ylabel('Food quality')
    ax.set_title('Tip values')
    ax.grid()
    fig.colorbar(cp, label='Tip in percents')
    fig.show()
    plt.pause(30)

def draw_plot(system):
    propina = system.compute(food=valorPrueba.food)



if __name__ == '__main__':
    main()
