from selenium import webdriver  # Importa el módulo principal de Selenium que permite controlar el navegador
from selenium.webdriver.common.by import By  # Importa la clase By para estrategias de localización


# Crea una instancia de opciones para configurar el comportamiento del navegador Chrome
chrome_options = webdriver.ChromeOptions()

# Engaña parcialmente a la web indicándole que nuestro navegador prefiere inglés y ubicación de USA
chrome_options.add_argument("--lang=en-US")
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

# Añade una opción experimental ('detach', True) que le dice al navegador que NO se cierre automáticamente 
# cuando el script termine de ejecutarse. Mantiene la ventana abierta para que podamos inspeccionarla.
chrome_options.add_experimental_option("detach", True)

# Inicializa el controlador (driver) de Chrome, pasándole las opciones configuradas previamente.
# Esto es lo que físicamente abre la ventana del navegador.
driver = webdriver.Chrome(options=chrome_options)

# Para forzar el cambio a USD, podemos inyectar una "cookie" (galletita de sesión) antes de cargar el producto.
# Primero debemos visitar el dominio raíz para que nos deje configurar la cookie
driver.get("https://www.amazon.com/")
driver.add_cookie({"name": "i18n-prefs", "value": "USD", "domain": ".amazon.com"})
driver.add_cookie({"name": "session-currency", "value": "USD", "domain": ".amazon.com"})

# Le indica al navegador que navegue a la URL especificada mediante una petición HTTP GET.
driver.get("https://www.amazon.com/Lenovo-ThinkBook-IRL-21SH000GUS-Computer/dp/B0F83ZRQM7/?currency=USD")

element = driver.find_element(By.CLASS_NAME, "a-offscreen")

price_float = element.get_attribute("textContent").strip("$")

print(price_float)

driver.quit()