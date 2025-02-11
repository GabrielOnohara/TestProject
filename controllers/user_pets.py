from db import Session
from models import User, Pet
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
import falcon


class UserPetsResource:
    def on_get(self, req, resp, user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).options(joinedload(User.pets)).one()
            pets = [{'name': pet.name, 'species': pet.species} for pet in user.pets]
            resp.media = pets
        except NoResultFound:
            resp.status = 404
            resp.media = {'error': 'User not found'}

        session.close()

    def on_post(self, req, resp, user_id):
        session = Session()
        try:
            user = session.query(User).filter(User.id == user_id).one()
            
            pet_data = req.media
            pet_name = pet_data.get('name')
            pet_species = pet_data.get('species')

            if not pet_name or not pet_species:
                resp.status = 400
                resp.media = {'error': 'Pet name and species are required'}
                return

            # Criando um novo pet e associando ao usuário
            new_pet = Pet(name=pet_name, species=pet_species)
            user.pets.append(new_pet)
            
            # Commitando a adição do pet
            session.add(new_pet)
            session.commit()

            # Retornar uma resposta de sucesso com o pet criado
            resp.status = falcon.HTTP_201
            resp.media = {
                'id': new_pet.id,
                'name': new_pet.name,
                'species': new_pet.species
            }

        except NoResultFound:
            resp.status = 404
            resp.media = {'error': 'User not found'}
        except Exception as e:
            resp.status = 500
            resp.media = {'error': f'An error occurred: {str(e)}'}
        finally:
            session.close()