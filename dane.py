from openpyxl import load_workbook
import matplotlib.pyplot as plt

wb = load_workbook('nowy_plik.xlsx')

sheet = wb['Sheet']
valueA1 = sheet['A1'].value
valueB1 = sheet['B1'].value
valueC1 = sheet['C1'].value

valueA2 = sheet['A2'].value
valueB2 = sheet['B2'].value
valueC3 = sheet['C3'].value

x = [valueA1, valueB1, valueC1]
y = ['A', 'B', 'C']

plt.bar(x,y)


plt.title('Wykres liniowy')
plt.xlabel('Oś X')
plt.ylabel('Oś y')
plt.show()
