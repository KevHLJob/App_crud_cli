#uso de paquete click 
import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Nombre del usuario')
@click.option('--lastname', required=True, help='Apellido del usuario')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('El nombre y el apellido son requeridos')
    else:
        data= json_manager.read_json()
        new_id = len(data) + 1
        new_user ={
            'id': new_id,
            'name': name,
            'lastname':lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} created successfully with Id: {new_id}")
        
@cli.command()
#muestra de datos json
def users():
    users =  json_manager.read_json()
    for user in users:
        print( f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
#list user with id
def user(id):
    data=json_manager.read_json()
    user= next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Usuario con Id {id} no encontrado")    
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")        
@cli.command()
@click.argument('id', type=int)
#delete function with id
def delete(id):
    data=json_manager.read_json()
    user= next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Usuario con Id {id} no encontrado")    
    else:
        data.remove(user)
        print(data)
        
if __name__ == '__main__':
    cli()
    
