import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def agregar_dispositivo(nombre, trabajo):
    payload = {"name": nombre, "job": trabajo}
    res = requests.post(BASE_URL, json=payload)
    return res

def listar_dispositivos():
    res = requests.get(BASE_URL)
    return res

def actualizar_dispositivo(id_user, nuevo_nombre, nuevo_trabajo):
    payload = {"name": nuevo_nombre, "job": nuevo_trabajo}
    res = requests.put(f"{BASE_URL}/{id_user}", json=payload)
    return res

def eliminar_dispositivo(id_user):
    res = requests.delete(f"{BASE_URL}/{id_user}")
    return res

if __name__ == "__main__":
    
    r_post = agregar_dispositivo("Raul", "Ingeniero")
    print("POST status:", r_post.status_code)
    print("POST response:", r_post.json())


    r_get = listar_dispositivos()
    print("GET status:", r_get.status_code)
    print("GET response:", r_get.json())

    
    r_put = actualizar_dispositivo(1, "Router1 ", "cisco2911")
    print("PUT status:", r_put.status_code)
    print("PUT response:", r_put.json())

    
    r_delete = eliminar_dispositivo(1)
    print("DELETE status:", r_delete.status_code)
    print("DELETE response:", r_delete.text)  
