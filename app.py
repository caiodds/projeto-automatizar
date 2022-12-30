import pyautogui
from time import sleep

# pyautogui.click(825,384,duration=2)
# pyautogui.write('caiolk')

# pyautogui.click(821,406,duration=2)
# pyautogui.write('1234')

# pyautogui.click(756,435,duration=2)

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(811,332,duration=2)
        pyautogui.write(produto)
        pyautogui.click(808,358,duration=2)
        pyautogui.write(quantidade)
        pyautogui.click(812,385,duration=2)
        pyautogui.write(preco)
        pyautogui.click(732,540,duration=1)