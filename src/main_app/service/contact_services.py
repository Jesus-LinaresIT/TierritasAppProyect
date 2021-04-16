from .. import DB as db
from ..model.user import Users, Contact


def save_contacts(data_contacts, id):

    Contacts = []
    for contact in data_contacts:
        if 'name' in contact and 'phone' in contact:
            if contact['name'].strip() != '' and contact['phone'].strip() != '':
                contact['user_id'] = id
                Contacts.append(Contact(contact))

    try:
        if len(Contacts) > 0:
            db.session.add_all(Contacts)
            db.session.commit()

    except:
        return {'message': 'Ocurrio un error al guardar los contactos de emergencia'}, 500


def edit_contact(data_contacts, id):

    for item in data_contacts:
        
        contact = None
        if 'id' in item:
            contact = Contact.query.filter_by(id=item['id']).first()

        if contact:
            
            if item['name'].strip() == '' or item['phone'].strip() == '':
                delete_one_contact(contact.id)            
            
            else:         
                       
                try:
                    contact.updateProperties(item)
                    db.session.commit()
                    
                except:
                    return {'message': 'Ha ocurrido un error al actualizar los contactos, por favor intente nuevamente'}, 500

        else:           
            save_contacts([item], id)

    return {'message': 'Contactos actualizados con éxito'}, 200
        


def delete_one_contact(id):
    user_contact = Contact.query.filter_by(id=id).first()
    if user_contact:
        try:
            db.session.delete(user_contact)
            db.session.commit()
            return {'message': 'Contacto eliminado con éxito'}, 200
        except:
            return {'message': 'Ha ocurrido un error al eliminar el contacto'}, 500
            
    return {'message' : 'Contact not found'}, 404

def get_contact(id):
    return Contact.query.filter_by(id=id).first()


def get_contacts(user_id):
    return Contact.query.filter_by(user_id=user_id).all()
