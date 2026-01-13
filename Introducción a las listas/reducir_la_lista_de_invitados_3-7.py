invitados = ['kentaro','akira','takehiko','yabako','eiichirō ']
print(f"Sr. {invitados[0].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[1].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[2].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[3].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[4].title()}, ha sido invitado a una cena en el Burj Khalifa.")

# Aviso y cambio de un invitado, despues las invitaciones .
print(f"\nEl Sr. {invitados[2].title()} no podra asistir.")
invitados[2] = 'shinichi'
print(f"Sr. {invitados[0].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[1].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[2].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[3].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[4].title()}, ha sido invitado a una cena en el Burj Khalifa.")

# Aviso de una mesa mas grande.
print("\nSe ha encontrado una mesa de comedor más grande.")
invitados.insert(0,'hideo')
invitados.insert(2,'hidetaka')
invitados.append('tatsuki')

# Mensajes de invitacion nuevos.
print(f"Sr. {invitados[0].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[1].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[2].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[3].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[4].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[5].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[6].title()}, ha sido invitado a una cena en el Burj Khalifa.")
print(f"Sr. {invitados[7].title()}, ha sido invitado a una cena en el Burj Khalifa.")

# Aviso del improvisto y eliminar los invitados que no van a la cena.
print("\nAviso de importancia: \nDebido a un imprevisto con la mesa solo habra espacio para dos invitados.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
invitado_fuera = invitados.pop()
print(f"Lo lamento Sr. {invitado_fuera} pero no podra asistir a la cena.")
print(f"\nSr. {invitados[0]} y el Sr. {invitados[1]} siguen en pie sus invitaciones.")

# Borrar los últimos dos nombres y imprirmir la lista.
del invitados[0]
del invitados[0]
print(invitados)