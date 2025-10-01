from domain.category import Category

def print_events(category: Category):
    print(f"--- Eventos para a categoria '{category.name}' ---")
    if not category.events:
        print("Nenhum evento registrado.")
    for event in category.events:
        print(f" - {event}")
    print("-" * 40)

    category.events.clear()

print(">>> 1. Criando uma nova categoria...")
c1 = Category(name="Filmes", description="Categoria para filmes de todos os gêneros")
print(f"Categoria criada: {c1}")
print_events(c1)

print("\n>>> 2. Serializando e reconstruindo o objeto...")
dict_c1 = c1.to_dict()
print(f"Objeto seralizado em dicionário\n{dict_c1}")

c2 = Category.from_dict(dict_c1)
print(f"Objeto reconstruído a partir do dicionário:\n{c2}")

c1_dict_no_events = c1.to_dict()
c2_dict_no_events = c2.to_dict()
are_equivalent = c1_dict_no_events == c2_dict_no_events
print(f"Os objetos c1 e c2 são equivalentes? {are_equivalent}")
print_events(c2)

print("\n>>> 3. Demonstrando o ciclo de vida da categoria...")

print("\nAtualizando nome e descrição...")
c1.update(name="Filmes e Séries", description="Categoria para filmes e séries")
print(f"Categoria atualizada: {c1}")
print_events(c1)

print("\nDesativando a categoria...")
c1.deactivate()
print(f"Categoria atualizada: {c1}")
print_events(c1)

print("\nTentando desativar novamente...")
c1.deactivate()
print_events(c1)

print("\nAtivando a categoria...")
c1.activate()
print(f"Categoria atualizada: {c1}")
print_events(c1)