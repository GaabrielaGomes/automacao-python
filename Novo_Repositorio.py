import pyautogui

#criando automação simples para criar um repositório no github
#Exemplo tendo duas contas no google

pyautogui.hotkey('win', 's') #Para abrir a função de pesquisa no S.O. Windows
pyautogui.sleep(1) #Pausa de 1 segundo
pyautogui.typewrite('google chrome', 0.1) #digita "google chrome". O valor 0.1 indica o intervalo entre a digitação de cada caractere.
pyautogui.press('enter') #Pressiona a tecla enter"
pyautogui.sleep(1)
pyautogui.moveTo(956, 641, duration = 2) #Para acessar a conta google escolhida
pyautogui.click()
pyautogui.sleep(2)
pyautogui.typewrite('https://github.com', 0.1) 
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.moveTo(1826, 140, duration = 2) #Posição do perfil
pyautogui.click()
pyautogui.moveTo(1658, 340, duration = 2) #Posição do repositório
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1702, 274, duration = 2) #Novo repositório
pyautogui.click()
pyautogui.sleep(1.5)
pyautogui.moveTo(962, 463, duration = 2) #Posição para adicionar nome ao repositório
pyautogui.click()
pyautogui.typewrite('automacao-python')
pyautogui.moveTo(524, 602, duration = 2) #Posição para adicionar descrição ao repositório
pyautogui.click()
pyautogui.typewrite('Repositorio criado a partir de uma automacao python', 0.1)
pyautogui.moveTo(496, 894, duration = 2) #Posição para adicionar README ao repositório
pyautogui.click()
pyautogui.press('enter')