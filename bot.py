from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador
driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver instalado

login_url = "https://amigosdelmatchedbetting.com/login/"
login_url = "https://amigosdelmatchedbetting.com/oddsmatcher-gratuito-2/"
# Cargar la página de inicio de sesión
driver.get(login_url)

# Llenar campos de inicio de sesión utilizando XPath
username_input = driver.find_element(By.XPATH, "//*[@id='user_login']")
password_input = driver.find_element(By.XPATH, "//*[@id='user_pass']")


username_input.send_keys("MatchedBetting226")
password_input.send_keys("MB3407-88")

# Hacer clic en el botón "ACCEDER"
login_button = driver.find_element(By.XPATH, "//*[@id='wp-submit']")
login_button.click()
time.sleep(6)

oddsmatcher_gratis = "https://amigosdelmatchedbetting.com/oddsmatcher-gratuito-2/"
# Cargar la página de inicio de sesión
driver.get(oddsmatcher_gratis)
time.sleep(5)
# Encontrar la tabla por su ID
table = driver.find_element(By.ID, "sbet_table")
# Recopilar las filas de la tabla
rows = table.find_elements(By.TAG_NAME, "tr")
# Imprimir los datos de la tabla
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    print("\t".join(row_data))

# Cerrar el navegador
driver.quit()
