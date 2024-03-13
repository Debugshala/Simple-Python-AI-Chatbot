import google.generativeai as gpt
prompt = input("Kya jaan na h bhai?")
gpt.configure(api_key='AIzaSyAFVBe0Z-WI-E2Xo2jdFX8uif8sbwyXJBc')
geminipro = gpt.GenerativeModel('gemini-pro')
response = geminipro.generate_content(prompt)
print(response.text)
